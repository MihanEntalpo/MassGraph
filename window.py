# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './window.ui'
#
# Created: Sun May 29 22:44:04 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(555, 470)
        self.groupBox = QtGui.QGroupBox(MainWindow)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 541, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 521, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.stateLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.stateLabel.setObjectName(_fromUtf8("stateLabel"))
        self.horizontalLayout_2.addWidget(self.stateLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.refreshPorts = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshPorts.sizePolicy().hasHeightForWidth())
        self.refreshPorts.setSizePolicy(sizePolicy)
        self.refreshPorts.setMaximumSize(QtCore.QSize(32, 32))
        self.refreshPorts.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshPorts.setIcon(icon)
        self.refreshPorts.setObjectName(_fromUtf8("refreshPorts"))
        self.horizontalLayout.addWidget(self.refreshPorts)
        self.ports = QtGui.QComboBox(self.verticalLayoutWidget)
        self.ports.setObjectName(_fromUtf8("ports"))
        self.horizontalLayout.addWidget(self.ports)
        self.connectPort = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectPort.sizePolicy().hasHeightForWidth())
        self.connectPort.setSizePolicy(sizePolicy)
        self.connectPort.setObjectName(_fromUtf8("connectPort"))
        self.horizontalLayout.addWidget(self.connectPort)
        self.disconnectPort = QtGui.QPushButton(self.verticalLayoutWidget)
        self.disconnectPort.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectPort.sizePolicy().hasHeightForWidth())
        self.disconnectPort.setSizePolicy(sizePolicy)
        self.disconnectPort.setObjectName(_fromUtf8("disconnectPort"))
        self.horizontalLayout.addWidget(self.disconnectPort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtGui.QGroupBox(MainWindow)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 541, 251))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.datalist = QtGui.QListWidget(self.groupBox_2)
        self.datalist.setGeometry(QtCore.QRect(10, 20, 331, 221))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.datalist.setFont(font)
        self.datalist.setObjectName(_fromUtf8("datalist"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 60, 181, 191))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.zeroKg = QtGui.QLineEdit(self.groupBox_3)
        self.zeroKg.setGeometry(QtCore.QRect(80, 20, 91, 23))
        self.zeroKg.setObjectName(_fromUtf8("zeroKg"))
        self.captureZero = QtGui.QPushButton(self.groupBox_3)
        self.captureZero.setGeometry(QtCore.QRect(10, 50, 161, 24))
        self.captureZero.setObjectName(_fromUtf8("captureZero"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.captureCoef = QtGui.QPushButton(self.groupBox_3)
        self.captureCoef.setGeometry(QtCore.QRect(10, 160, 161, 24))
        self.captureCoef.setObjectName(_fromUtf8("captureCoef"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.coef = QtGui.QLineEdit(self.groupBox_3)
        self.coef.setGeometry(QtCore.QRect(80, 80, 91, 23))
        self.coef.setObjectName(_fromUtf8("coef"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 71, 41))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.measureMass = QtGui.QLineEdit(self.groupBox_3)
        self.measureMass.setGeometry(QtCore.QRect(80, 130, 91, 23))
        self.measureMass.setObjectName(_fromUtf8("measureMass"))
        self.timeToZero = QtGui.QPushButton(self.groupBox_2)
        self.timeToZero.setGeometry(QtCore.QRect(350, 30, 171, 23))
        self.timeToZero.setObjectName(_fromUtf8("timeToZero"))
        self.groupBox_4 = QtGui.QGroupBox(MainWindow)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 370, 531, 91))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.fileNameInput = QtGui.QLineEdit(self.groupBox_4)
        self.fileNameInput.setGeometry(QtCore.QRect(90, 30, 401, 21))
        self.fileNameInput.setObjectName(_fromUtf8("fileNameInput"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.fileNameButton = QtGui.QPushButton(self.groupBox_4)
        self.fileNameButton.setGeometry(QtCore.QRect(500, 30, 21, 23))
        self.fileNameButton.setObjectName(_fromUtf8("fileNameButton"))
        self.startWriteButton = QtGui.QPushButton(self.groupBox_4)
        self.startWriteButton.setGeometry(QtCore.QRect(60, 60, 121, 23))
        self.startWriteButton.setObjectName(_fromUtf8("startWriteButton"))
        self.stopWriteButton = QtGui.QPushButton(self.groupBox_4)
        self.stopWriteButton.setEnabled(False)
        self.stopWriteButton.setGeometry(QtCore.QRect(190, 60, 151, 23))
        self.stopWriteButton.setObjectName(_fromUtf8("stopWriteButton"))
        self.openFileButton = QtGui.QPushButton(self.groupBox_4)
        self.openFileButton.setGeometry(QtCore.QRect(350, 60, 121, 23))
        self.openFileButton.setObjectName(_fromUtf8("openFileButton"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MassGraph", None))
        self.groupBox.setTitle(_translate("MainWindow", "Подключение", None))
        self.label.setText(_translate("MainWindow", "Состояние:", None))
        self.stateLabel.setText(_translate("MainWindow", "Отключено", None))
        self.refreshPorts.setToolTip(_translate("MainWindow", "Обновить список портов", None))
        self.ports.setToolTip(_translate("MainWindow", "Список портов", None))
        self.connectPort.setText(_translate("MainWindow", "Подключить", None))
        self.disconnectPort.setText(_translate("MainWindow", "Отключить", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Данные", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Масштабирование", None))
        self.zeroKg.setText(_translate("MainWindow", "8000000", None))
        self.captureZero.setText(_translate("MainWindow", "Засечь ноль", None))
        self.label_2.setText(_translate("MainWindow", "Ноль кг.:", None))
        self.captureCoef.setText(_translate("MainWindow", "Засечь коэффициент", None))
        self.label_3.setText(_translate("MainWindow", "Коэфф.:", None))
        self.coef.setText(_translate("MainWindow", "-0.01", None))
        self.label_4.setText(_translate("MainWindow", "Масса для замера:", None))
        self.measureMass.setText(_translate("MainWindow", "1", None))
        self.timeToZero.setText(_translate("MainWindow", "Сбросить время на 0", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Файл", None))
        self.fileNameInput.setText(_translate("MainWindow", "./output.csv", None))
        self.label_5.setText(_translate("MainWindow", "Имя файла:", None))
        self.fileNameButton.setText(_translate("MainWindow", "...", None))
        self.startWriteButton.setText(_translate("MainWindow", "Начать запись", None))
        self.stopWriteButton.setText(_translate("MainWindow", "Остановить запись", None))
        self.openFileButton.setText(_translate("MainWindow", "Открыть файл", None))

import res_rc
