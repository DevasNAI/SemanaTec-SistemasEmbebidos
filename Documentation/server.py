from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/sensores/temp',methods=['GET'])
def getTemp():
    try:
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