# Ultrasonic Distance Sensor Using Arduino

## Objective

To learn how to measure the distance of an object using an HC-SR04 ultrasonic sensor and Arduino Uno.

## Description

In this activity, an HC-SR04 ultrasonic distance sensor is connected to an Arduino Uno.

The sensor sends ultrasonic sound waves towards an object and receives the reflected sound waves. Arduino measures the time taken for the echo to return and uses this time to calculate the distance.

The measured distance is displayed on the Serial Monitor.

---

## Components Required

- Arduino Uno
- HC-SR04 Ultrasonic Distance Sensor
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

### What is an Ultrasonic Sensor?

An ultrasonic sensor measures distance using sound waves that are too high-pitched for humans to hear.

The HC-SR04 sends a short burst of ultrasonic sound waves towards an object.

When the sound waves hit the object, they are reflected back towards the sensor.

The sensor measures the time taken for the echo to return.

The Grade 8 book explains that the HC-SR04 typically uses ultrasonic sound at around 40 kHz and calculates distance from the echo time. :contentReference[oaicite:1]{index=1}

---

## HC-SR04 Pins

The HC-SR04 has four pins:

| Pin  | Purpose                       |
| ---- | ----------------------------- |
| VCC  | Power supply                  |
| GND  | Ground                        |
| TRIG | Sends the trigger signal      |
| ECHO | Receives the reflected signal |

The book specifies VCC as 5V and describes the TRIG and ECHO pins as the signal pins. :contentReference[oaicite:2]{index=2}

---

## How Distance is Measured

The Arduino sends a short HIGH pulse to the TRIG pin.

The sensor then sends ultrasonic pulses.

When the pulses hit an object, they bounce back to the sensor.

The ECHO pin stays HIGH for the time taken by the ultrasonic wave to travel to the object and return.

Arduino measures this time using:

```cpp
pulseIn(echoPin, HIGH);
```
