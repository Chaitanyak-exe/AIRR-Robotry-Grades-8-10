# Circuit Connections

## LED Connections

Each LED is connected to an Arduino digital output pin through a 220Ω resistor.

### Red LED

| Component     | Terminal    | Connect To        |
| ------------- | ----------- | ----------------- |
| Arduino Uno   | D11         | 220Ω resistor     |
| 220Ω resistor | Other end   | Red LED Anode (+) |
| Red LED       | Cathode (-) | GND               |

### Yellow LED

| Component     | Terminal    | Connect To           |
| ------------- | ----------- | -------------------- |
| Arduino Uno   | D10         | 220Ω resistor        |
| 220Ω resistor | Other end   | Yellow LED Anode (+) |
| Yellow LED    | Cathode (-) | GND                  |

### Green LED

| Component     | Terminal    | Connect To          |
| ------------- | ----------- | ------------------- |
| Arduino Uno   | D9          | 220Ω resistor       |
| 220Ω resistor | Other end   | Green LED Anode (+) |
| Green LED     | Cathode (-) | GND                 |

---

## Complete Connection Table

| LED    | Arduino Pin | Resistor | Other LED Terminal |
| ------ | ----------: | -------: | ------------------ |
| Red    |         D11 |     220Ω | Cathode → GND      |
| Yellow |         D10 |     220Ω | Cathode → GND      |
| Green  |          D9 |     220Ω | Cathode → GND      |

The Grade 8 book specifies red, yellow and green LEDs on pins 11, 10 and 9 respectively, using 220Ω resistors, with all LED cathodes connected to GND. :contentReference[oaicite:6]{index=6}

---

## Connection Flow

### Red LED

Arduino D11

↓

220Ω resistor

↓

Red LED Anode (+)

↓

Red LED Cathode (-)

↓

GND

---

### Yellow LED

Arduino D10

↓

220Ω resistor

↓

Yellow LED Anode (+)

↓

Yellow LED Cathode (-)

↓

GND

---

### Green LED

Arduino D9

↓

220Ω resistor

↓

Green LED Anode (+)

↓

Green LED Cathode (-)

↓

GND

---

## Arduino Pin Summary

| Arduino Pin | Connected Component | Function      |
| ----------: | ------------------- | ------------- |
|         D11 | Red LED             | STOP          |
|         D10 | Yellow LED          | READY         |
|          D9 | Green LED           | GO            |
|         GND | All LED cathodes    | Common ground |

---

## Important

- Use one 220Ω resistor for each LED.
- Check LED polarity before powering the circuit.
- The longer LED leg is normally the anode (+).
- The shorter LED leg is normally the cathode (-).
- Make sure all LED cathodes are connected to Arduino GND.
- Do not connect an LED directly to an Arduino output without a current-limiting resistor.
