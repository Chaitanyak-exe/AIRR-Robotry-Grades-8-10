# IR Object Detection Using Arduino

## Objective

To detect the presence of an object using an IR sensor and Arduino Uno.

## Description

In this activity, an IR object detection sensor is connected to an Arduino Uno.

The IR sensor sends infrared light and detects the reflected light from a nearby object.

When an object is detected, the sensor sends a digital signal to the Arduino. Arduino reads this signal and turns ON an LED.

When the object is removed, the LED turns OFF.

---

## Components Required

- Arduino Uno
- IR Object Detection Sensor
- LED
- 220Ω resistor
- Breadboard
- Jumper wires
- USB cable
- Laptop

For complete component details, see [components.md](components.md).

---

## Software Required

- Arduino IDE
- Arduino Uno board support

---

## Theory

### What is an IR Sensor?

An IR sensor uses infrared light to detect objects.

An IR sensor generally contains:

- IR LED / emitter
- Receiver / photodiode

The IR emitter sends infrared light toward the object.

When the infrared light is reflected from the object, the receiver detects the reflected light.

The sensor then produces an output signal.

Robotry explains that an IR proximity sensor can detect whether an object is present or absent using a digital HIGH/LOW output. :contentReference[oaicite:1]{index=1}

---

## How Object Detection Works

```text
IR Sensor
    ↓
Sends infrared light
    ↓
Light hits object
    ↓
Light is reflected
    ↓
Sensor detects reflection
    ↓
Digital output changes
    ↓
Arduino reads the output
    ↓
LED turns ON
```
