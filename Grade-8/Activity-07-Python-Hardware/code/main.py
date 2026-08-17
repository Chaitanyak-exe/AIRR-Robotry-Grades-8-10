import pyfirmata
import time

# Connect to Arduino
board = pyfirmata.Arduino('/dev/ttyACM0')

# Set up LED pin 13
led = board.get_pin('d:13:o')

print('Blinking LED from Python!')

for i in range(10):
    led.write(1)
    time.sleep(0.5)

    led.write(0)
    time.sleep(0.5)

board.exit()

print('Done!')