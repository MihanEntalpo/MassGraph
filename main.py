import sys
import os
import re
import serial
import threading
import time
import datetime
import subprocess
import yaml
from PyQt4 import QtCore, QtGui, uic
from window import Ui_MainWindow

#скорость передачи данных
SPEED = 230400

class RealWindow(QtGui.QDialog):
    def __init__(self, app, ui: Ui_MainWindow):
        """
        :type app: MyApp
        """
        super().__init__()
        self.app = app
        self.ui = ui
        self.ui.setupUi(self)
        self.ui.datalist.setUniformItemSizes(True)

        self.fill_ports()
        self.attach_handlers()
        self.first_time = time.time()
        self.file_descriptor = None

        self.conf = self.load_conf()
        self.init_conf()

        self.capture_in_progress = False
        self.captured_nums_count = 0
        self.captured_nums_avg = 0


    def attach_handlers(self):
        self.ui.refreshPorts.clicked.connect(self.fill_ports)
        self.ui.connectPort.clicked.connect(self.connect_click)
        self.ui.disconnectPort.clicked.connect(self.disconnect_click)
        self.app.serial.line_readed.connect(self.data_arrived)

        self.ui.captureZero.pressed.connect(self.captureZeroBegin)
        self.ui.captureZero.released.connect(self.captureZeroEnd)

        self.ui.captureCoef.pressed.connect(self.captureCoefBegin)
        self.ui.captureCoef.released.connect(self.captureCoefEnd)

        self.ui.startWriteButton.clicked.connect(self.startWriteFile)
        self.ui.stopWriteButton.clicked.connect(self.stopWriteFile)
        self.ui.openFileButton.clicked.connect(self.openFile)

        self.ui.timeToZero.clicked.connect(self.timeToZero)

    def update_conf(self):
        self.conf["coef"] = float(self.ui.coef.text())
        self.conf["zero"] = float(self.ui.zeroKg.text())
        self.conf["measure_mass"] = float(self.ui.measureMass.text())
        self.conf["filename"] = self.ui.fileNameInput.text()

    def init_conf(self):
        coef = self.conf.get("coef", 100)
        zero = self.conf.get("zero", 8000000)
        measureMass = self.conf.get("measure_mass", 1)
        filename = self.conf.get("filename", "./output.csv")
        self.ui.coef.setText(str(coef))
        self.ui.zeroKg.setText(str(zero))
        self.ui.measureMass.setText(str(measureMass))
        if os.path.exists(filename):
            namepart, extpart = os.path.splitext(filename)
            matches = re.search("(?P<full>_(?P<num>[0-9]+))", namepart)
            if matches:
                num = int(matches.groupdict()['num'])
                full_num = matches.groupdict()['full']
                numless_name = namepart[0:-len(full_num)]
            else:
                num = 1
                numless_name = namepart

            filename_full = numless_name + "_" + str(num + 1) + extpart

            self.ui.fileNameInput.setText(filename_full)

        else:
            self.ui.fileNameInput.setText(filename)


    def load_conf(self):
        conf = {}
        if os.path.exists("./config.yml"):
            with open("./config.yml", "r") as f:
                conf = yaml.load(f)
        return conf

    def timeToZero(self):
        if self.ui.stopWriteButton.isEnabled():
            QtGui.QMessageBox.warning(self, "Ошибка", "Идёт запись в файл! Нельзя сбросить время!")
        self.first_time = time.time()

    def save_conf(self, conf):
        with open("./config.yml", "w") as f:
            yaml.dump(conf, f)

    def beginMeasure(self):
        self.captured_nums_avg = 0
        self.captured_nums_count = 0
        self.capture_in_progress = True

    def endMeasure(self):
        self.capture_in_progress = False
        if self.captured_nums_count == 0:
            return None
        else:
            return self.captured_nums_avg

    def measure(self, num):
        if self.capture_in_progress:
            self.captured_nums_avg = (
                (self.captured_nums_avg * self.captured_nums_count + num) / (self.captured_nums_count + 1)
            )
            self.captured_nums_count += 1

    def captureZeroBegin(self):
        self.beginMeasure()

    def captureZeroEnd(self):
        measured = self.endMeasure()
        if measured is not None:
            self.ui.zeroKg.setText(str(round(measured, 4)))

    def captureCoefBegin(self):
        self.beginMeasure()

    def captureCoefEnd(self):
        measured = self.endMeasure()
        nonZeroKg = self.get_number(self.ui.measureMass)
        if measured is not None and measured != 0 and nonZeroKg != 0:
            zeroKg = self.get_number(self.ui.zeroKg)
            coef = round((measured - zeroKg) / nonZeroKg, 3)
            self.ui.coef.setText(str(round(coef, 9)))

    def startWriteFile(self):
        if not self.app.serial.serial.isOpen():
            QtGui.QMessageBox.warning(self, "Ошибка", "Подключение не установлено!")
        else:
            filename = self.ui.fileNameInput.text()
            try:
                if os.path.exists(filename):
                    f = open(filename, "a")
                else:
                    f = open(filename, "w")
                    f.write("\ufeff")
                    f.write("Время;Секунд прошло;Масса;Сырое значение;\n")
                self.file_descriptor = f
            except PermissionError as e:
                QtGui.QMessageBox.warning(self, "Ошибка создания фала", str(e))

            self.ui.fileNameInput.setEnabled(False)
            self.ui.startWriteButton.setEnabled(False)
            self.ui.stopWriteButton.setEnabled(True)

    def stopWriteFile(self):
        if self.file_descriptor is None:
            QtGui.QMessageBox.warning(self, "Ошибка", "Файл не был открыт")
        else:
            self.file_descriptor.close()
            self.file_descriptor = None
            self.ui.fileNameInput.setEnabled(True)
            self.ui.startWriteButton.setEnabled(True)
            self.ui.stopWriteButton.setEnabled(False)

    def openFile(self):
        filename = self.ui.fileNameInput.text()
        if not os.path.exists(filename):
            QtGui.QMessageBox.warning(self, "Ошибка", "Файл не существует")
        else:
            fullpath = os.path.realpath(filename)
            print(fullpath)
            process = subprocess.Popen(['xdg-open',fullpath])

    def data_arrived(self, s):
        try:
            num = int(s.decode("UTF-8"))
            self.number_arrived(num)
        except ValueError as e:
            print("ValueError: " + str(e))

    def number_arrived(self, num):
        self.measure(num)
        self.add_line(0, num, num)

    def get_number(self, lineedit):
        try:
            v = float(lineedit.text())
        except ValueError as e:
            v = 0
            print("ValueError: " + str(e))
        return v

    def get_mass(self, num):
        coef = self.get_number(self.ui.coef)
        zeroKg = self.get_number(self.ui.zeroKg)
        kg = round((num - zeroKg) / coef, 4)
        return kg

    def add_line(self, timestamp, num, num_adjusted):
        t = round(time.time() - self.first_time,3)

        kg = self.get_mass(num)
        s = "{:<6} {:>12} {:>12} кг".format(t, num, kg)
        self.ui.datalist.addItem(s)
        self.ui.datalist.scrollToBottom()
        if self.file_descriptor is not None:
            self.file_descriptor.write("{};{};{};{};\n".format(
                datetime.datetime.now(),
                str(t).replace(".",","),
                str(kg).replace(".",","),
                num))

    def fill_ports(self):
        self.ui.ports.clear()
        for port in self.app.serial.get_ports():
            self.ui.ports.addItem(port)

    def closeEvent(self, QCloseEvent):
        self.update_conf()
        self.save_conf(self.conf)
        self.app.suicide()

    def connect_click(self):
        port = self.ui.ports.currentText()
        if port:
            self.app.serial.open_connection(port)

            self.ui.refreshPorts.setEnabled(False)
            self.ui.ports.setEnabled(False)
            self.ui.connectPort.setEnabled(False)
            self.ui.disconnectPort.setEnabled(True)

        else:
            QtGui.QMessageBox.warning(self, "Ошибка", "Вы не выбрали порт!")

    def disconnect_click(self):
        self.ui.refreshPorts.setEnabled(True)
        self.ui.ports.setEnabled(True)
        self.ui.connectPort.setEnabled(True)
        self.ui.disconnectPort.setEnabled(False)
        self.app.serial.close_connection()

class Serial(QtCore.QObject):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.serial = serial.Serial()
        self.read_thread = None
        self.stop_thread_event = None

    def open_connection(self, port, speed=SPEED):
        self.serial.port = "/dev/" + port
        self.serial.baudrate = speed
        self.serial.open()
        if self.read_thread is not None:
            self.stop_thread_event.set()
            self.read_thread.join(1)
        self.stop_thread_event = threading.Event()
        self.read_thread = threading.Thread(target = self.read_loop, args=(self.stop_thread_event,))
        self.read_thread.start()

    def read_loop(self, stop_event):
        print("read loop started")
        while not stop_event.is_set():
            if self.serial.isOpen():
                try:
                    line = self.serial.readline()
                except serial.serialutil.SerialException as e:
                    if ("device reports readiness to read but returned no data" in str(e)):
                        pass
                    else:
                        raise e
                self.data_arrived(line)
        print("read loop stopped")

    def close_connection(self):
        self.stop_thread_event.set()
        self.read_thread.join(1)
        self.serial.close()
        if self.serial.isOpen():
            print("Serial is not closed, as it should be!")

    @staticmethod
    def get_ports():
        ports = []
        for path, files, dirs in os.walk("/sys/class/tty"):
            for file in files:
                fullname = "/sys/class/tty/" + file
                link = os.readlink(fullname)
                if re.search("/usb[0-9]+/", link):
                    ports.append(file)
            break
        return ports

    def data_arrived(self, line):
        self.line_readed.emit(line)

    line_readed = QtCore.pyqtSignal(bytes)

class MyApp(QtGui.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.serial = Serial(self)

    def suicide(self):
        if self.serial.serial.isOpen():
            self.serial.close_connection()
        self.quit()


app = MyApp(sys.argv)

window = RealWindow(app, Ui_MainWindow())
window.show()

app.exec_()