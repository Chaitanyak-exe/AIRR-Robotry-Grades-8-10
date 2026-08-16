# Circuit Connections

## Arduino Uno to LED

The LED is connected to Arduino digital pin D13 through a 220Ω resistor.

| Component | Terminal | Connect To |
|---|---|---|
| Arduino Uno | D13 | 220Ω resistor |
| 220Ω resistor | Other end | LED Anode (+) |
| LED | Cathode (-) | Arduino GND |

---

## Connection Flow

```text
Arduino D13
    │
    │
    ▼
220Ω Resistor
    │
    │
    ▼
LED Anode (+)
    │
    │
   LED
    │
    │
    ▼
LED Cathode (-)
    │
    │
    ▼
Arduino GND