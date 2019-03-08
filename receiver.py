from microbit import *

import radio

radio.config(channel=20)
radio.on()

uart.init(baudrate=9600)

while True:
    msg = radio.receive()
    if msg:
        uart.write(msg)