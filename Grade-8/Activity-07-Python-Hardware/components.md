# Components Required

## Hardware Components

| No. | Component   | Quantity | Purpose                                            |
| --: | ----------- | -------: | -------------------------------------------------- |
|   1 | Arduino Uno |        1 | Receives commands from Python and controls the LED |
|   2 | USB Cable   |        1 | Provides communication between Arduino and laptop  |
|   3 | Laptop      |        1 | Runs Python and controls the Arduino               |

## Built-in Component

### Arduino Built-in LED

Arduino Uno has a built-in LED connected to digital pin 13.

This LED is used in this activity, so an external LED and resistor are not required.

## Software

| Software    | Purpose                                   |
| ----------- | ----------------------------------------- |
| Arduino IDE | Uploads StandardFirmata to Arduino        |
| Python 3    | Runs the control program                  |
| PyFirmata   | Allows Python to communicate with Arduino |

Install PyFirmata using:

```bash
pip install pyfirmata
```
