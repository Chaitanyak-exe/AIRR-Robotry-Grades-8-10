# Components Required

## Hardware Components

| No. | Component                 |    Quantity | Purpose                      |
| --: | ------------------------- | ----------: | ---------------------------- |
|   1 | Arduino Uno               |           1 | Main controller              |
|   2 | L298N Motor Driver Module |           1 | Controls both DC motors      |
|   3 | DC Gear Motor             |           2 | Drives the two wheels        |
|   4 | Wheels                    |           2 | Provides movement            |
|   5 | Robot Chassis             |           1 | Holds the robot components   |
|   6 | Castor Wheel              |           1 | Provides balance and support |
|   7 | HC-SR04 Ultrasonic Sensor |           1 | Detects obstacles            |
|   8 | 9V Battery + Connector    |           1 | Supplies motor power         |
|   9 | Jumper Wires              | As required | Electrical connections       |
|  10 | Small Breadboard          |           1 | Used for sensor connections  |
|  11 | USB Cable                 |           1 | Connects Arduino to laptop   |
|  12 | Laptop                    |           1 | Used to program Arduino      |

The Grade 8 equipment list specifically includes the Arduino Uno, HC-SR04, L298N, two DC motors with wheels and 9V battery for these builds. :contentReference[oaicite:15]{index=15}

---

## Component Details

### Arduino Uno

Arduino Uno is the main controller.

It reads the HC-SR04 distance and sends control signals to the L298N motor driver.

### L298N Motor Driver

The L298N controls two independent motor channels.

- Motor A controls the left motor.
- Motor B controls the right motor.

The ENA and ENB pins provide PWM speed control.

### DC Motors

Two DC motors provide the driving force.

One motor is installed on the left side and the other on the right side.

### Wheels

The wheels are attached to the DC motors and allow the robot to move.

### Castor Wheel

The castor wheel is a passive support wheel.

It helps keep the robot balanced.

### HC-SR04

The HC-SR04 measures the distance between the robot and an obstacle.

### 9V Battery

The battery supplies power for the motor driver and motors.

### Chassis

The chassis provides the mechanical frame for mounting the components.

### Jumper Wires

Jumper wires connect the Arduino, L298N and ultrasonic sensor.

### Breadboard

The breadboard can be used for the HC-SR04 connections.

### USB Cable

The USB cable is used to upload the Arduino program.

### Laptop

The laptop is used with Arduino IDE to write and upload the program.
