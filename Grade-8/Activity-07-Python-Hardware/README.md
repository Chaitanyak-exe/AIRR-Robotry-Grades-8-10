# Python-Controlled LED from Laptop

## Objective

To control an Arduino LED using Python running on a laptop.

## Description

In this activity, Python is used to control an Arduino Uno through a USB connection.

Normally, Arduino is programmed using its own C++ language. In this activity, Python running on the laptop communicates with Arduino using the Firmata protocol.

The Arduino is first programmed with StandardFirmata. After that, Python uses the PyFirmata library to send commands to the Arduino.

The built-in LED connected to Arduino pin 13 is controlled from Python.

---

## Components Required

- Arduino Uno
- USB cable
- Laptop

For complete details, see [components.md](components.md).

---

## Software Required

- Arduino IDE
- Python 3
- PyFirmata Python library

Install PyFirmata using:

```bash
pip install pyfirmata
```
