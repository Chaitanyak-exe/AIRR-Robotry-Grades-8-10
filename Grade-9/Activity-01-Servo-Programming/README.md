# Servo Programming Using Arduino

## Objective

To control the position of a servo motor using an Arduino Uno and the Servo.h library.

## Description

A servo motor can rotate to a specific angle and hold its position.

In this activity, an Arduino Uno controls a servo motor using the built-in Servo.h library.

The servo is connected to Arduino pin 9.

The program moves the servo smoothly from 0° to 180° and then back from 180° to 0°.

This activity introduces the basic programming of servo motors using Arduino.

## Components Required

- Arduino Uno
- Servo Motor
- Jumper wires
- USB cable
- Laptop

For complete details, see [components.md](components.md).

## Software Required

- Arduino IDE
- Arduino Uno board support
- Servo.h library

The Servo.h library is included with the Arduino IDE and does not need to be downloaded separately. The Grade 9 book explains that the library handles the PWM signal generation automatically. :contentReference[oaicite:1]{index=1}

---

## Theory

### What is a Servo Motor?

A servo motor is a motor designed for precise positional control.

Unlike a normal DC motor that continuously rotates, a servo can be commanded to move to a particular angle.

For example:

```text
0°   → One extreme
90°  → Centre
180° → Other extreme
```
