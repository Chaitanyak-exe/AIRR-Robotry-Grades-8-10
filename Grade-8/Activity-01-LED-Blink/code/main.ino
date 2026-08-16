void setup() {
pinMode(13, OUTPUT); // Set pin 13 as an output
}
void loop() {
digitalWrite(13, HIGH); // Turn LED ON (5V on pin 13)
delay(1000); // Wait 1000 milliseconds = 1 second
digitalWrite(13, LOW); // Turn LED OFF (0V on pin 13)
delay(1000); // Wait 1 second
}