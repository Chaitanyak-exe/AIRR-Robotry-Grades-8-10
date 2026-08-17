# 2WD Obstacle Avoiding Robot

## Objective

To build a two-wheel-drive robot using Arduino Uno, an L298N motor driver and an HC-SR04 ultrasonic sensor.

The robot moves forward and automatically avoids obstacles detected in front of it.

## Description

A 2WD (Two-Wheel Drive) robot has two independently driven wheels, one on each side, and a passive castor wheel for balance.

In this activity, Arduino controls two DC motors through an L298N motor driver.

An HC-SR04 ultrasonic sensor is used to detect obstacles in front of the robot.

When there is no nearby obstacle, the robot moves forward.

When an obstacle is detected within 20 cm, the robot:

1. Stops.
2. Turns left.
3. Continues moving forward.

This activity combines motor control, ultrasonic sensing and Arduino programming.

---

## Components Required

- Arduino Uno
- L298N Motor Driver Module
- DC Motors × 2
- Wheels × 2
- Robot chassis
- Castor wheel
- HC-SR04 Ultrasonic Distance Sensor
- 9V battery and connector
- Jumper wires
- Small breadboard
- USB cable
- Laptop

See [components.md](components.md) for complete details.

The Grade 8 book lists the Arduino Uno, L298N, two DC motors with wheels, 9V battery, HC-SR04 and jumper wires for the 2WD robot build. :contentReference[oaicite:2]{index=2}

---

## Software Required

- Arduino IDE
- Arduino Uno board support

---

## Theory

### What is a 2WD Robot?

A 2WD robot has two driven wheels.

One motor controls the left wheel and another motor controls the right wheel.

A passive castor wheel supports the robot.

```text
             FRONT

       ┌───────────────┐
       │   HC-SR04     │
       └───────────────┘

       O             O
    Left Motor    Right Motor

              ○
          Castor Wheel
```
