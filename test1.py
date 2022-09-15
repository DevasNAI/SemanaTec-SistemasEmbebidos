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
ids = 1

registros = [
  {'id': 1, 'temperature':"value", 'time':"time-stamp", 'stable': "stability"},
  {'id': 2, 'temperature':"value", 'time':"time-stamp", 'stable': "stability"}
]

class Registros():
    """
        Clase Registros
        Esta clase actua como una estructura de datos que guarda
        un ID, temperatura, tiempo y estabilidad.
        Variables privadas:
        int     ID              |    Representa el indice
        float   temperature     |    Un valor de temperatura
        string  time            |    Marca de Tiempo en formato string
        bool    stable          |    Marca si la temperatura es estable o no
    """

    def __init__(self, id, temperature):
        """
            Constructor Registros
            Recibe un id y un valor de temperatura
            int     ID              |    Representa el indice
            float   temperature     |    Un valor de temperatura
        """
        self.id = id
        self.temperature = temperature
        self.time = datetime.now()
        if(temperature > 28.9):
            self.stable = False
        else:
            self.stable = True
    #   Cambia la temperatura
    def setTemp(temp):
        temperature = temp
    #   Regresa la temperatura
    def getTemp(self):
        return self.temperature
    #   Regresa el ID
    def getId(self):
        return self.id
    #   Regresa la temperatura en formato de grados C
    def getTempString(self):
        return str(self.temperature) + " C"
    #   Cambia el ID
    def setId(self, nid):
        id = nid
    #   Regresa el tiempo
    def getTime(self):
        return self.time
    #   Regresa la estabilidad
    def getStable(self):
        return self.stable
    def getRegister(self):
        return {'id': str(self.id), 'temperature': str(self.temperature) + "° C", 'time': str(self.time), 'stable': str(self.stable)}


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
    registrado = Registros(ids, 27).getRegister()
    registros.append(registrado)
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

#   Borrar los datos de temperatura
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
    app.run(host="127.0.0.1", port=5000)