from flask import Flask
from flask import request, jsonify
import time

app = Flask(__name__)



    
#   Prueba de registros
registros = [
  {'id': 1, 'temperature':"value", 'time':"time-stamp", 'stable': "stability"},
  {'id': 2, 'temperature':"value", 'time':"time-stamp", 'stable': "stability"}
]
print(type(registros))
#   Muestra la página principal
@app.route("/")
def hello():
    return "Conexión exitosa: Datos de Clínica A405"

#   Muestra los datos de la temperatura
@app.route('/updated-temperature',methods=['GET'])
def getTemp():
    try:
        #   Retorna los registros de temperatura
        return jsonify( registros )
    except (IOError, TypeError) as e:
        return jsonify({"error": e})

#   En teoría debe borrar los datos de temperatura
@app.route('/updated-temperature',methods=['DELETE'])
def delTemp(id):
    try:
        registros.pop(id)
        return jsonify( {"temp": 20} )
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
    app.run(host="0.0.0.0", port=5000)