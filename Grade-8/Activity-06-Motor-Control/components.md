# Components Required

## Hardware Components

| No. | Component                   |    Quantity | Purpose                            |
| --: | --------------------------- | ----------: | ---------------------------------- |
|   1 | Arduino Uno                 |           1 | Sends control signals to the L298N |
|   2 | L298N Motor Driver          |           1 | Controls the motor direction       |
|   3 | DC Gear Motor               |           1 | Provides rotary motion             |
|   4 | External Motor Power Supply |           1 | Supplies power to the motor        |
|   5 | Jumper Wires                | As required | Makes electrical connections       |
|   6 | USB Cable                   |           1 | Connects Arduino to laptop         |
|   7 | Laptop                      |           1 | Used to program Arduino            |

## Component Details

### Arduino Uno

Arduino Uno is the controller.

It sends digital HIGH and LOW signals to the L298N input pins.

### L298N Motor Driver

The L298N is used to control the DC motor.

It receives control signals from Arduino and supplies the motor with current from the external motor supply.

### DC Gear Motor

The DC motor converts electrical energy into rotary motion.

### External Motor Power Supply

The motor should be powered using a suitable external supply rather than directly from an Arduino GPIO pin.

### Jumper Wires

Jumper wires are used to connect Arduino, L298N and the motor.

### USB Cable

The USB cable connects the Arduino to the laptop and allows the program to be uploaded.

### Laptop

The laptop is used to:

- Write the Arduino program.
- Upload the program.
- Test the motor control.
