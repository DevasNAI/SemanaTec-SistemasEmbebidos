# --- SERVER API --- #
import json
from flask import Flask
from flask import request, jsonify
import time

# --- HARDWARE --- #
import time, math                                                                                                                                                                                                      
import grovepi                                                                                                                                                                                                          
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


def sensoring():
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
        setText(str(temp))
        time.sleep(2)
        setText("")


app = Flask(__name__)



#   Prueba de registros
registros = [
  {'id': 1, 'temperature':"value", 'time':"time-stamp", 'stable': "stability"},
  {'id': 2, 'temperature':"value", 'time':"time-stamp", 'stable': "stability"}
]
# print(type(registros))


# Muestra la pagina principal
@app.route("/")
def hello():
    sensoring()
    return "Conexion exitosa: Datos de Clinica A405"

#   Muestra los datos de la temperatura
@app.route('/updated-temperature',methods=['GET'])
def getTemp():
    try:
        sensoring()
        return jsonify( registros )
    except (IOError, TypeError) as e:
        return jsonify({"error": e})

# @app.route('/updated-temperature/<int:id>',methods=['GET'])
# def getTemp(id):
#     try:
#         #   Retorna un solo registro de temperatura
#         item = [reg for reg in registros if reg["id"] == id]
#         return jsonify( item[0] )
#     except (IOError, TypeError) as e:
#         return jsonify({"error": e})

#   En teoría debe borrar los datos de temperatura
@app.route('/updated-temperature/<int:id>',methods=['DELETE'])
def delTemp(id):
    try:
        item = [reg for reg in registros if reg["id"] == id]
        registros.remove(item[0])
        return jsonify( item[0] )


    except (IOError, TypeError) as e:
        return jsonify({"error": e})

# @app.route('/sensores/lcd',methods=['PUT'])
# def setLCD():
#     try:
#         print(request.json)
#         texto = request.json["texto"]
#         return jsonify( {"texto": texto} )
#     except (IOError, TypeError) as e:
#         return jsonify({"error": e})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)