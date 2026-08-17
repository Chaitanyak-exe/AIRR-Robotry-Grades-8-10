# Circuit Connections

## HC-SR04 Connections

The HC-SR04 is connected to the Arduino Uno using four connections.

| HC-SR04 Pin | Arduino Connection | Purpose        |
| ----------- | ------------------ | -------------- |
| VCC         | 5V                 | Power supply   |
| GND         | GND                | Ground         |
| TRIG        | D9                 | Trigger signal |
| ECHO        | D10                | Echo signal    |

These are the connections specified for the HC-SR04 distance activity in the Grade 8 book. :contentReference[oaicite:7]{index=7}

---

## Connection Flow

```text
HC-SR04 VCC
     │
     ▼
Arduino 5V


HC-SR04 GND
     │
     ▼
Arduino GND


HC-SR04 TRIG
     │
     ▼
Arduino D9


HC-SR04 ECHO
     │
     ▼
Arduino D10
```
