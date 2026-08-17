# Components Required

## Hardware Components

| No. | Component    | Quantity | Purpose                           |
| --: | ------------ | -------: | --------------------------------- |
|   1 | Arduino Uno  |        1 | Controls the servo motor          |
|   2 | Servo Motor  |        1 | Provides precise angular movement |
|   3 | Jumper Wires |        3 | Connects the servo to Arduino     |
|   4 | USB Cable    |        1 | Connects Arduino to laptop        |
|   5 | Laptop       |        1 | Used to program Arduino           |

---

## Component Details

### Arduino Uno

Arduino Uno is the main controller used in this activity.

It runs the program and sends control signals to the servo.

### Servo Motor

The servo motor is used for precise angular movement.

The Arduino can command the servo to move to a particular angle.

The Grade 9 book describes the servo as a component that can be controlled to exact angles using Arduino code. :contentReference[oaicite:7]{index=7}

### Jumper Wires

Three jumper wires are used to connect:

- Signal
- Power
- Ground

### USB Cable

The USB cable connects the Arduino Uno to the laptop.

It is used to upload the Arduino program and provide power to the Arduino.

### Laptop

The laptop is used to:

- Write the Arduino program.
- Upload the program.
- Open the Serial Monitor.
- Observe the servo operation.

---

## Software

| Software    | Purpose                      |
| ----------- | ---------------------------- |
| Arduino IDE | Write and upload the program |
| Servo.h     | Control the servo motor      |

The `Servo.h` library is included with the Arduino IDE. It handles the PWM signal generation needed for servo control. :contentReference[oaicite:8]{index=8}
