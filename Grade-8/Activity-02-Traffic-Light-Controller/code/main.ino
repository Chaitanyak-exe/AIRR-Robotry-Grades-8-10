// Traffic Light Controller
const int redPin = 9;
const int yellowPin = 10;
const int greenPin = 11;
void setup() {
pinMode(redPin, OUTPUT);
pinMode(yellowPin, OUTPUT);
pinMode(greenPin, OUTPUT);
}
void loop() {
// Red phase — STOP
digitalWrite(redPin, HIGH);
digitalWrite(yellowPin, LOW);
digitalWrite(greenPin, LOW);
delay(3000); // Red for 3 seconds
// Yellow phase — READY
digitalWrite(redPin, LOW);
digitalWrite(yellowPin, HIGH);
delay(1000); // Yellow for 1 second
// Green phase — GO
digitalWrite(yellowPin, LOW);
digitalWrite(greenPin, HIGH);
delay(3000); // Green for 3 seconds
// Yellow again before red
digitalWrite(greenPin, LOW);
digitalWrite(yellowPin, HIGH);
delay(1000);
}