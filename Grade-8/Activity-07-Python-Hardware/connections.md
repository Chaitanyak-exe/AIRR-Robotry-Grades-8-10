# Connections

## Hardware Connection

This activity uses the Arduino Uno's built-in LED.

No external LED circuit is required.

| Arduino      | Connection      |
| ------------ | --------------- |
| USB Port     | Laptop USB Port |
| Built-in LED | Digital Pin 13  |

## Connection Diagram

```text
┌─────────────────┐
│     Laptop      │
│                 │
│  Python Program │
└────────┬────────┘
         │
         │ USB
         │
         ▼
┌─────────────────┐
│   Arduino Uno   │
│                 │
│ Digital Pin 13  │
│       ↓         │
│  Built-in LED   │
└─────────────────┘
```
