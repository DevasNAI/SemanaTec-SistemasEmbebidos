import json
from flask import Flask
from flask import request, jsonify
import time
from datetime import datetime

app = Flask(__name__)
ids = 1
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
        return str(self.temperature) + "C"
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
        return {'id': str(self.id), 'temperature': str(self.temperature) + "C", 'time': str(self.time), 'stable': str(self.stable)}



#   Prueba de registros
registros = [
    Registros(ids, 27).getRegister(),
    Registros(ids+1, 29).getRegister(),
    {"id":3,"stable":"True","temperature":"27 C","time":"2022-09-15 02:09:03.471549"},
    {"id":4,"stable":"True","temperature":"27 C","time":"2022-09-15 02:09:10.561097"},
    {"id":5,"stable":"True","temperature":"27 C","time":"2022-09-15 02:09:13.742259"},
    {"id":6,"stable":"True","temperature":"27 C","time":"2022-09-15 02:09:19.342881"},
    {"id":7,"stable":"True","temperature":"27 C","time":"2022-09-15 02:09:23.010771"},
    {"id":8,"stable":"True","temperature":"27 C","time":"2022-09-15 02:09:26.753546"},
    {"id":9,"stable":"True","temperature":"27 C","time":"2022-09-15 02:09:43.745423"},
    {"id":10,"stable":"True","temperature":"27 C","time":"2022-09-15 02:10:54.095374"}
]

#   Muestra la pagina principal
@app.route("/")
def hello():
    return "Conexion exitosa: Datos de Clinica A405"

#   Muestra los datos de la temperatura
@app.route('/updated-temperature',methods=['GET'])
def getTemp():
    try:
        #   Retorna los registros de temperatura
        return jsonify( registros )
    except (IOError, TypeError) as e:
        return jsonify({"error": e})

# Borrar los datos de temperatura
@app.route('/updated-temperature/<int:id>',methods=['DELETE'])
def delTemp(id):
    try:
        item = [reg for reg in registros if reg["id"] == id]
        registros.remove(item[0])
        return jsonify( item[0] )


    except (IOError, TypeError) as e:
        return jsonify({"error": e})



@app.route('/sensores/lcd',methods=['PUT'])
def setLCD():
    try:
        print(request.json)
        texto = request.json["texto"]
        return jsonify( {"texto": texto} )
    except (IOError, TypeError) as e:
        return jsonify({"error": e})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)