# Reading a Pushbutton Using Arduino

## Objective

To learn how to use a push button as a digital input and control an LED based on the button state.

## Description

In this activity, a push button is connected to an Arduino Uno digital input pin.

When the button is pressed, the Arduino detects the input and turns the LED ON. When the button is released, the LED turns OFF.

This activity introduces the concept of digital input and shows how Arduino can read the state of an external device.

## Components Required

- Arduino Uno
- Push button
- LED
- 220Ω resistor
- Breadboard
- Jumper wires
- USB cable
- Laptop

For complete component details, see [components.md](components.md).

## Software Required

- Arduino IDE
- Arduino Uno board support

## Theory

### What is a Push Button?

A push button is a simple digital input device.

When the button is pressed, it connects its terminals together. When it is released, the connection is broken.

The Arduino can detect whether the button is pressed or released by reading the electrical state of a digital input pin.

### Digital Input

Arduino digital pins can be used as inputs or outputs.

When a pin is configured as a digital input, Arduino reads its electrical state.

A digital input has two basic states:

- HIGH
- LOW

The `digitalRead()` function is used to read the state of a digital input pin.

### INPUT_PULLUP

Arduino has a built-in pull-up resistor that can be enabled using:

```cpp
pinMode(buttonPin, INPUT_PULLUP);
```
