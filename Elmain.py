
import time, math                                                                                                                                                                                                      
import grovepi               
from flask import Flask
from flask import request, jsonify
import time
from grovepi import * 
from grove_rgb_lcd import *                                                                                                                                                                                                    
                                                                                                                                                                                                                     
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
        # LCD
        setRGB(0,0,255)
        setText("")

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
            time.sleep(.5)
        else:
            digitalWrite(led,0)             # Send LOW to switch off LED
            print ("LED OFF!")
            time.sleep(.5)
        

        # Show Temperature
        if (grovepi.digitalRead(touch_sensor)==1):
            print(temp)
            # print(math.ceil(temp))
            # print(str(math.ceil(temp)))
            # print(format(str(math.ceil(temp))))
            # upperTemp = int(math.ceil(temp))
            # print(upperTemp)
            setText(str(temp))
            time.sleep(2)
            setText("")
        

                                                                                                                                                                         
    except KeyboardInterrupt:
        digitalWrite(led,0)
        break
    except IOError:
        print ("Error")