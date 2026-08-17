// 2WD Obstacle Avoiding Robot
// Motor A = Left
// Motor B = Right

const int ENA = 5;
const int IN1 = 6;
const int IN2 = 7;

const int ENB = 10;
const int IN3 = 8;
const int IN4 = 9;

const int TRIG = 2;
const int ECHO = 3;

const int SAFE_DISTANCE = 20;

void setup() {

  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  Serial.begin(9600);

  Serial.println("2WD Robot Ready!");
}

long getDistance() {

  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);

  digitalWrite(TRIG, LOW);

  return pulseIn(ECHO, HIGH) / 58;
}

void moveForward(int spd) {

  analogWrite(ENA, spd);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  analogWrite(ENB, spd);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void turnLeft(int spd) {

  analogWrite(ENA, 0);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  analogWrite(ENB, spd);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void stopMotors() {

  analogWrite(ENA, 0);
  analogWrite(ENB, 0);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void loop() {

  long dist = getDistance();

  Serial.print("Distance: ");
  Serial.print(dist);
  Serial.println(" cm");

  if (dist > SAFE_DISTANCE) {

    moveForward(180);

  } else {

    stopMotors();
    delay(300);

    turnLeft(180);
    delay(600);

    stopMotors();
    delay(200);
  }
}