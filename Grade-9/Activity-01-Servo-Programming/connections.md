# Circuit Connections

## Servo Motor Connections

A typical servo motor has three connections:

| Servo Wire / Pin | Arduino Connection | Purpose              |
| ---------------- | ------------------ | -------------------- |
| Signal           | D9                 | Servo control signal |
| Power            | 5V                 | Servo power          |
| Ground           | GND                | Common ground        |

The Grade 9 book specifies the servo signal connection to an Arduino pin, red wire to 5V and brown/black wire to GND. :contentReference[oaicite:9]{index=9}

---

## Connection Diagram

```text
                 Arduino Uno
              ┌──────────────┐
              │              │
        D9 ───┤              │
              │              │
        5V ───┤              │
              │              │
       GND ───┤              │
              └──────┬───────┘
                     │
                     │
                     ▼
              ┌─────────────┐
              │    SERVO    │
              │             │
              │ Signal       │
              │ Power        │
              │ Ground       │
              └─────────────┘
```
