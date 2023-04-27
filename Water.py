# Write your code here :-)
from microbit import *
import math

# Declare a function of MIDI Control Change (CC) event.
def midiControlChange(chan, n, value):
    MIDI_CC = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_CC | chan, n, value])
    uart.write(msg)

# Function to send MIDI data through cable
def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

Start()
last_cond = 0  # Initialise a variable with initial value for conductivity
last_temp = 0  # Initialise a variable with initial value for temperature
while True:
    cond = pin2.read_analog()  # Read the conductivity value from pin2
    if last_cond != cond:  # Compare the current value with the last value
        # Amplify & Scale the conductivity value to a number between 0 & 127
        velocity = math.floor((cond * 6.0) / 1024 * 127)
        midiControlChange(0, 23, velocity)  # send its value through MIDI CC event
    last_cond = cond  # Set the last reading value to the current reading value
    sleep(100)  # Sleep for 100ms and repeat the while loop

    temp = pin1.read_analog()  # Read the temperature value from pin1
    if last_temp != temp:  # Compare the current value with the last value
        # Scale the temperature value to a number between 0 & 127
        celsius = math.floor(temp / 1024 * 127)
        midiControlChange(0, 22, celsius)  # send its value through MIDI CC event
    last_temp = temp  # Set the last reading value to the current reading value
    sleep(100)  # Sleep for 100ms and repeat the while loop







