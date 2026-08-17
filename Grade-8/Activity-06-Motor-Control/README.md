# Simple Motor Control Using Arduino and L298N

## Objective

To control the direction and movement of a DC motor using an Arduino Uno and an L298N motor driver.

## Description

In this activity, an Arduino Uno is connected to an L298N motor driver.

The L298N acts as an interface between the Arduino and the DC motor. Arduino sends control signals to the L298N, and the driver supplies the required current to the motor.

The motor is controlled in two directions:

- Forward
- Reverse

The Arduino program changes the motor direction by changing the input signals of the L298N.

---

## Components Required

- Arduino Uno
- L298N Motor Driver Module
- DC Gear Motor × 1
- External motor power supply
- Breadboard or connecting wires
- Jumper wires
- USB cable
- Laptop

For complete details, see [components.md](components.md).

---

## Software Required

- Arduino IDE
- Arduino Uno board support

---

## Theory

### Why is a Motor Driver Required?

An Arduino pin cannot directly supply the amount of current normally required by a DC motor.

A motor driver is therefore used between the Arduino and the motor.

The L298N receives low-power control signals from the Arduino and controls the motor using the external motor power supply.

```text
Arduino
   ↓
Control Signals
   ↓
L298N Motor Driver
   ↓
DC Motor
```
