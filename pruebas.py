import time
import grovepi
 
# Connect the Grove Touch Sensor to digital port D2
# SIG,NC,VCC,GND
touch_sensor = 2
 
grovepi.pinMode(touch_sensor,"INPUT")
 
while True:
    try:
        print(grovepi.digitalRead(touch_sensor))
        time.sleep(.5)
 
    except IOError:
        print ("Error")
