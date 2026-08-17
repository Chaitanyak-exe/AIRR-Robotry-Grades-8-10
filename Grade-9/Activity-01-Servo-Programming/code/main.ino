#include <Servo.h>

Servo myServo;

const int servoPin = 9;

void setup() {

  myServo.attach(servoPin);

  Serial.begin(9600);
  Serial.println("Servo ready!");
}

void loop() {

  // Sweep from 0 to 180 degrees
  for (int angle = 0; angle <= 180; angle += 1) {

    myServo.write(angle);

    delay(15);
  }

  delay(500);

  // Sweep back from 180 to 0 degrees
  for (int angle = 180; angle >= 0; angle -= 1) {

    myServo.write(angle);

    delay(15);
  }

  delay(500);
}