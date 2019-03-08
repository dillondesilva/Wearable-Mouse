from microbit import *
import radio

radio.config(channel=20)

radio.on()
# if z i greater than 0, swipe is occuring left
# if y is greater than 700, mouse goes up
# if x is less than -700, mouse goes left > 110
# if y is less than -200, mosue goes down
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    
    if z > 0:
        radio.send("swipe\n")
    
    if y > 700:
        radio.send("up\n")
        
    if y < -200:
        radio.send("down\n")
        
    if x < -700:
        radio.send("left\n")
        
    if x > 110:
        radio.send("right\n")
    
    print (x, y, z)
    sleep(10)