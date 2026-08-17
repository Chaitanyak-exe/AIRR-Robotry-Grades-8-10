# Circuit Connections

## L298N Motor Driver Connections

The Grade 8 book uses the following connections:

| L298N Pin | Arduino Pin | Purpose               |
| --------- | ----------: | --------------------- |
| ENA       |          D5 | Left motor speed      |
| IN1       |          D6 | Left motor direction  |
| IN2       |          D7 | Left motor direction  |
| ENB       |         D10 | Right motor speed     |
| IN3       |          D8 | Right motor direction |
| IN4       |          D9 | Right motor direction |

These pin assignments are taken directly from the Grade 8 2WD robot wiring guide. :contentReference[oaicite:16]{index=16}

---

## Motor Connections

### Left Motor

Connect the left DC motor to:

```text
L298N OUT1
     │
     ├── Left Motor
     │
L298N OUT2
```
