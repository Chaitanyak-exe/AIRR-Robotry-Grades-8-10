# Circuit Connections

## IR Sensor Connections

| IR Sensor Pin | Arduino Connection | Purpose               |
| ------------- | ------------------ | --------------------- |
| VCC           | 5V                 | Power                 |
| GND           | GND                | Ground                |
| OUT           | D2                 | Digital sensor signal |

---

## LED Connections

| LED Terminal | Connection                |
| ------------ | ------------------------- |
| Anode (+)    | D13 through 220Ω resistor |
| Cathode (-)  | GND                       |

---

## Complete Connection Table

| Component | Pin / Terminal | Arduino Connection        |
| --------- | -------------- | ------------------------- |
| IR Sensor | VCC            | 5V                        |
| IR Sensor | GND            | GND                       |
| IR Sensor | OUT            | D2                        |
| LED       | Anode (+)      | D13 through 220Ω resistor |
| LED       | Cathode (-)    | GND                       |

---

## Connection Flow

### IR Sensor

```text
IR Sensor VCC
      │
      ▼
Arduino 5V

IR Sensor GND
      │
      ▼
Arduino GND

IR Sensor OUT
      │
      ▼
Arduino D2
```
