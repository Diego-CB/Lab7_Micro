# ------------------------------------------------------
# Universidad del Valle de Guatemala
# Programacion de Microprocesadores
#
# Laboratorio 7:
# - Lectura de datos de multiples sensores 
#   y escritura de archivo Json
# 
# Autores:
# - Diego Cordova, 20212
# - Alejandro Gomez, 20347
# - Paola de Leon, 
# ------------------------------------------------------

# librerias importadas
import time
import json
import adafruit_dht
import board
import datetime as dt

# Objetos de sensores
dht = adafruit_dht.DHT11(board.D4)

# Diccionario para agregar datos
sensorData = {}
sensorData["DHT11"] = []

# ------------------------ Lectura de sensores ------------------------

for i in range(0, 20):

    # --------------- Sensor de humedad DHT11 ---------------
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        deltaTime = dt.datetime.now().strftime('%H:%M:%S')

        if humidity is None or temperature is None:
            raise RuntimeError

        sensorData["DHT11"].append({
            'temp' : str(temperature),
            'humedad' : str(humidity),
            'time' : deltaTime
        })

        print(f"Temp: {temperature} ºC \t Humidity: {humidity}% \t Time: {deltaTime}")
        
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        #print("Reading from DHT failure: ", e.args)
        pass

    time.sleep(1)

# -------------- Escritura de Json --------------

newJson = json.dumps(sensorData, indent=4)

with open('newJson', 'w') as outfile:
    outfile.write(newJson)
