#include <Q2HX711.h>

Q2HX711 hx711(A1, A0);

const int led = 2;

int state = 0;

void setup() {
  Serial.begin(115200);
  digitalWrite(led, HIGH);
}

void blink()
{
  state = !state;
  if (state)
  {
    digitalWrite(led, HIGH);
  }
  else
  {
    digitalWrite(led, LOW);
  }
}

void loop() {
  Serial.println(hx711.read());
}
