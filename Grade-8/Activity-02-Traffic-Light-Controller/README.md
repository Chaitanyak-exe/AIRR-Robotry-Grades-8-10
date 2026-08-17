# Traffic Light Controller Using Arduino

## Objective

To build a simple traffic light controller using Arduino and three LEDs representing the red, yellow, and green traffic signals.

---

## Description

In this activity, an Arduino Uno is used to control three LEDs.

The three LEDs represent:

- Red — STOP
- Yellow — READY
- Green — GO

The Arduino turns the LEDs ON and OFF in a fixed sequence.

The sequence is:

Red → Yellow → Green → Yellow → Repeat

This activity demonstrates digital output, timing, and basic control logic using Arduino.

---

## Components Required

- Arduino Uno
- Red LED
- Yellow LED
- Green LED
- 220Ω resistors × 3
- Breadboard
- Jumper wires
- USB cable
- Laptop

For more information, see [components.md](components.md).

---

## Software Required

- Arduino IDE
- Arduino Uno board support

---

## Theory

### What is a Traffic Light?

A traffic light is a signalling system used to control the movement of vehicles and pedestrians.

A normal traffic signal uses three lights:

- **Red** — Stop
- **Yellow** — Get ready / wait
- **Green** — Go

In this activity, LEDs are used to represent these three signals.

---

## Digital Output

Arduino digital pins can be configured as outputs.

When a digital output is set to:

- `HIGH` — the output is turned ON
- `LOW` — the output is turned OFF

The Arduino uses the `digitalWrite()` function to control the LEDs.

The book explains that digital output can be used to control LEDs and other devices. :contentReference[oaicite:1]{index=1}

---

## Delay and Timing

The `delay()` function pauses the Arduino program for a specified amount of time.

For example:

```cpp
delay(3000);
```
