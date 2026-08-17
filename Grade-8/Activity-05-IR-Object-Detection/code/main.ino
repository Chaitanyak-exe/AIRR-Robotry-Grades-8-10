const int irPin = 2;
const int ledPin = 13;

void setup() {
  pinMode(irPin, INPUT);
  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  int sensorState = digitalRead(irPin);

  if (sensorState == LOW) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Object Detected!");
  }
  else {
    digitalWrite(ledPin, LOW);
    Serial.println("No Object");
  }

  delay(200);
}