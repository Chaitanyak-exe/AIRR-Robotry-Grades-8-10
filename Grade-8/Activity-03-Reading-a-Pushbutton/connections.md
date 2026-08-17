# Circuit Connections

## Push Button Connections

The push button is connected between Arduino digital pin D2 and GND.

The Arduino's internal pull-up resistor is used, so an external pull-up resistor is not required.

| Component   | Terminal       | Connect To  |
| ----------- | -------------- | ----------- |
| Push Button | One terminal   | Arduino D2  |
| Push Button | Other terminal | Arduino GND |

## LED Connections

The LED is connected to Arduino digital pin D13 through a 220Ω resistor.

| Component     | Terminal    | Connect To    |
| ------------- | ----------- | ------------- |
| Arduino Uno   | D13         | 220Ω resistor |
| 220Ω resistor | Other end   | LED Anode (+) |
| LED           | Cathode (-) | Arduino GND   |

## Complete Connection Table

| Component   | Pin / Terminal | Arduino Connection        |
| ----------- | -------------- | ------------------------- |
| Push Button | Terminal 1     | D2                        |
| Push Button | Terminal 2     | GND                       |
| LED         | Anode (+)      | D13 through 220Ω resistor |
| LED         | Cathode (-)    | GND                       |

## Connection Flow

### Push Button

```text
Arduino D2
    │
    ▼
Push Button
    │
    ▼
Arduino GND
```
