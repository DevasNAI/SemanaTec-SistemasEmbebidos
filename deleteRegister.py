import json
from flask import Flask
from flask import request, jsonify
import time
from datetime import datetime

#app = Flask(__name__)
global ids
ids = 0
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
        return {'id': self.id, 'temperature': str(self.temperature) + "C", 'time': str(self.time), 'stable': str(self.stable)}



#   Prueba de registros
global registros
registros = [
    Registros(ids+1, 27).getRegister(),
    Registros(ids+2, 29.8).getRegister(),
    Registros(ids+3, 29.3).getRegister(),
    Registros(ids+4, 29.2).getRegister(),
    Registros(ids+5, 28).getRegister(),
    Registros(ids+6, 27.5).getRegister(),
    Registros(ids+7, 27.3).getRegister(),
    Registros(ids+8, 27.8).getRegister(),
    Registros(ids+9, 27.9).getRegister(),
    Registros(ids+10, 28).getRegister()
]


id = 1

for j in registros:
    print(j)

# for j in registros:
#     print(j)
item = [reg for reg in registros if reg["id"] == id]
# print(item, "Hola")
registros.remove(item[0])
# print(registros)

tempa = list(range(1, len(registros)+1))
print(tempa)

print(registros, "\n Cuchau\n")





for j in registros:
    print(j)

def updateDeletedID():
    i = 0
    #   Definimos un rango de lista auxiliar para actualizar los valores de ID
    listRange = list(range(len(registros)+1))
    #   Iteramos en los registros
    for j in registros:
        #   Si el id de uno de los registros es diferente al valor en listRange
        if(j['id'] != listRange[i] ):
            #   Actualiza el valor actual de ID
            j['id'] = listRange[i]

        else:
            continue
        #   Incrementa la variable de iteración
        i += 1
    print("La base de datos ha sido actualizada")






# Borrar los datos de temperatura
#@app.route('/updated-temperature/<int:id>',methods=['DELETE'])
#def delTemp(id):
#    try:
#        item = [reg for reg in registros if reg["id"] == id]
#        registros.remove(item[0])
#        return jsonify( item[0] )


 #   except (IOError, TypeError) as e:
  #      return jsonify({"error": e})

