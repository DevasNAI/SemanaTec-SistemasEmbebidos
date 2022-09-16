import time
import grovepi
from grovepi import *


# sensor touch
#####################################################################
 
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
    ###################################################################
# sensor temperatura
########################################################################

# Connect the Grove Temperature Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 0
 
while True:
    try:
        temp = grovepi.temp(sensor,'1.1')
        print("temp =", temp)
        time.sleep(.5)
 
    except KeyboardInterrupt:
        break
    except IOError:
        print( "Error" )

#############################################################################
#LED Socket
############################################################################
# GrovePi LED Blink example
 
# Connect the Grove LED to digital port D4
led = 4
 
pinMode(led,"OUTPUT")
time.sleep(1)
 
while True:
    try:
        #Blink the LED
        digitalWrite(led,1)     # Send HIGH to switch on LED
        time.sleep(1)
 
        digitalWrite(led,0)     # Send LOW to switch off LED
        time.sleep(1)
 
    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print "Error"
