# LED Blink Using Arduino

## Objective

To learn how to control an LED using an Arduino Uno and understand the basic concept of digital output.

---

## Description

In this activity, an LED is connected to an Arduino Uno through a resistor. A simple Arduino program is used to turn the LED ON and OFF repeatedly.

This is a basic Arduino activity that helps students understand how a microcontroller can control an electronic component.

---

## Components Required

- Arduino Uno
- LED
- 220Ω resistor
- Breadboard
- Jumper wires
- USB cable
- Laptop

For more details, see [components.md](components.md).

---

## Software Required

- Arduino IDE
- Arduino Uno board support

---

## Theory

### What is an LED?

LED stands for **Light Emitting Diode**. It is an electronic component that produces light when electric current flows through it in the correct direction.

An LED has two terminals:

- **Anode (+)** – positive terminal
- **Cathode (-)** – negative terminal

The longer leg of a standard LED is usually the anode, while the shorter leg is usually the cathode.

### What is Arduino?

Arduino Uno is a microcontroller development board that can be programmed to control electronic components.

It can receive inputs from components such as buttons and sensors and control outputs such as LEDs, motors and buzzers.

### What is Digital Output?

A digital output can have two basic states:

- **HIGH** – ON
- **LOW** – OFF

In this activity, Arduino uses a digital pin to control the LED.

When the pin is HIGH, the LED turns ON.

When the pin is LOW, the LED turns OFF.

### Why is a Resistor Used?

A resistor is connected in series with the LED to limit the current flowing through it.

This helps protect the LED from excessive current.

### How Does the Activity Work?

The Arduino program performs the following sequence:

1. Set the LED pin as an output.
2. Set the pin HIGH.
3. The LED turns ON.
4. Wait for one second.
5. Set the pin LOW.
6. The LED turns OFF.
7. Wait for one second.
8. Repeat the process.

Because these instructions are inside the `loop()` function, the LED continues blinking.

---

## Circuit Diagram

![LED Blink Circuit](circuit/circuit.png)

---

## Connections

For the circuit used in this activity:

| Component | Terminal    | Arduino Connection                |
| --------- | ----------- | --------------------------------- |
| LED       | Anode (+)   | Arduino D13 through 220Ω resistor |
| LED       | Cathode (-) | Arduino GND                       |

For the complete connection details, see [connections.md](connections.md).

---

## Procedure

1. Collect the Arduino Uno, LED, 220Ω resistor, breadboard and jumper wires.
2. Place the LED on the breadboard.
3. Connect the LED anode to one side of the 220Ω resistor.
4. Connect the other side of the resistor to Arduino digital pin D13.
5. Connect the LED cathode to Arduino GND.
6. Connect the Arduino Uno to the laptop using the USB cable.
7. Open Arduino IDE.
8. Select the correct Arduino board and port.
9. Enter the LED Blink program.
10. Verify and upload the program.
11. Observe the LED.
12. The LED should turn ON and OFF repeatedly.

---

## Source Code

The source code is available in:

[`code/main.ino`](code/main.ino)
