import time                                                                                                                                                                                                          
import grovepi                                                                                                                                                                                                          
from grovepi import *                                                                                                                                                                                                     
                                                                                                                                                                                                                     
# Connect the Grove Touch Sensor to digital port D4                                                                                                                                                                  
# SIG,NC,VCC,GND                                                                                                                                                                                                     
touch_sensor = 4 
# Connect the Grove Temperature Sensor to analog port A0
# SIG,NC,VCC,GND
temp_sensor = 0 
# Connect the Grove LED to digital port D4
led = 3
                                                                                                                                                                         
grovepi.pinMode(touch_sensor,"INPUT")   

pinMode(led,"OUTPUT")                                                                                                                                                                                                
time.sleep(1)
                                                                                                                                                                                                                     
while True:                                                                                                                                                                                                          
    try:   
        #Touch Sensor                                                                                                                                                                                                          
        print(grovepi.digitalRead(touch_sensor))

        #Temp Sensor
        temp = grovepi.temp(temp_sensor,'1.1')
        print("temp =", temp)
        time.sleep(.5) 

        #Blink the LED
        if (temp>=28):
            digitalWrite(led,1)             # Send HIGH to switch on LED
            print ("LED ON!")
            time.sleep(1)
        else:
            digitalWrite(led,0)             # Send LOW to switch off LED
            print ("LED OFF!")
            time.sleep(1)

                                                                                                                                                                         
    except KeyboardInterrupt:
        digitalWrite(led,0)
        break
    except IOError:
        print ("Error")