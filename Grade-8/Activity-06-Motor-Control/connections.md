# Circuit Connections

### Arduino to L298N

| Arduino Pin | L298N Pin | Purpose                 |
| ----------- | --------- | ----------------------- |
| D8          | IN1       | Motor direction control |
| D9          | IN2       | Motor direction control |
| 5V          | ENA       | Enables Motor A         |
| 5V          | 5VEN      | Enable/logic connection |
| GND         | GND       | Common ground           |

### Motor

| L298N Pin | Connection       |
| --------- | ---------------- |
| OUT1      | Motor terminal 1 |
| OUT2      | Motor terminal 2 |

### Power Supply

| Power Connection | Connected To            |
| ---------------- | ----------------------- |
| Battery positive | L298N motor power input |
| Battery negative | L298N GND               |
| Arduino GND      | L298N GND               |

Arduino GND, battery negative and L298N GND share a common ground.

## Motor Control Logic

| IN1  | IN2  | Motor   |
| ---- | ---- | ------- |
| LOW  | LOW  | Stop    |
| HIGH | LOW  | Forward |
| LOW  | HIGH | Reverse |

The actual physical direction depends on the motor wiring.

## Important

- Do not connect the motor directly to Arduino pins.
- The motor is powered through the L298N driver.
- Use the external battery/power supply for the motor.
- Arduino GND, battery negative and L298N GND must share a common ground.
- ENA must be enabled for Motor A.

## Connection Flow

```text
              Arduino
             ┌─────────┐
        D8 ──│         │
        D9 ──│         │
       GND ──│         │
             └────┬────┘
                  │
                  ▼
            ┌───────────┐
            │   L298N   │
            │           │
        IN1 │           │
        IN2 │           │
       GND  │           │
            │           │
      OUT1 ─┼───────────┼── Motor
      OUT2 ─┼───────────┼── Motor
            └───────────┘
                  ▲
                  │
          External Motor
             Power Supply
```
