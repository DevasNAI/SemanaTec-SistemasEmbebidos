from datetime import datetime

class Registros():
    """
        Clase Registros
        Esta clase actúa como una estructura de datos que guarda
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
        return str(self.temperature) + "° C"
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

        



print(Registros(1, 25).getRegister())
