# Circuit Connections

## Arduino Uno to LED

The LED is connected to Arduino digital pin D13 through a 220Ω resistor.

| Component     | Terminal    | Connect To    |
| ------------- | ----------- | ------------- |
| LED           | Anode (+)   | 220Ω resistor |
| 220Ω resistor | Other end   | Arduino D13   |
| LED           | Cathode (-) | Arduino GND   |

---

## Connection Flow

```text
Arduino D13
    │
    │
  220Ω
 Resistor
    │
    │
 LED Anode (+)
    │
   LED
    │
 LED Cathode (-)
    │
    │
 Arduino GND
```
