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
# - Paola de Leon, 20361
# ------------------------------------------------------

# librerias importadas
from os import error
import time
import json
import adafruit_dht #sensor Diego Cordova
import adafruit_sht31d #sensor Alejandro Gomez
import board
import datetime as dt

# Diccionario para agregar datos
sensorData = {}
sensorData["DHT11"] = [] #Sensor DHT11 
sensorData["SHT31D"] = [] #Sensor SHT31-D

def GuardarJSON(type):
    newJson = json.dumps(sensorData, indent=4)

    with open('newJson.json', 'w') as outfile:
        outfile.write(newJson)
    
    print('\nArchivo Json escrito con exito!!\n')


def SensorDHT11():
    # ------------------------ Lectura de sensores ------------------------

    try:
        dht = adafruit_dht.DHT11(board.D4)

    except Exception:
        pass

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
        GuardarJSON()



def SensorSTH31D():
    # ------------------------ Lectura de sensores ------------------------

    try:
        sht = adafruit_sht31d.SHT31D(board.I2C())
        
    except Exception:
        pass

    for i in range(0, 20):
                # --------------- Sensor de temperatura/humedad STH31 ---------------
        try:
            temperature = sht.temperature
            humidity = sht.relative_humidity
            deltaTime = dt.datetime.now().strftime('%H:%M:%S')

            if humidity is None or temperature is None:
                raise RuntimeError

            sensorData["SHT31D"].append({
                'temp' : str(temperature),
                'humedad' : str(humidity),
                'time' : deltaTime
            })

            print(f"Temp: {temperature} ºC \t Humidity: {humidity}% \t Time: {deltaTime}")
            
        except RuntimeError as e:
            # Reading doesn't always work! Just print error and we'll try again
            #print("Reading from DHT failure: ", e.args)
            pass

        time.sleep(2)
        GuardarJSON()



def Menu1():
    # Variable de menu
    salir = False
    print("Bienvenido al Laboratorio No.7")
    # Ciclo del menu
    while salir == False:
        # Se muestran las opciones del menú
        print("\nQue desea hacer? ")
        print("1) Usar sensor DTH11")
        print("2) Usar sensor STH31D")
        print("3) Salir")

        opcion = input("\nIngrese su opción: ")
        # Se verifica si se ingresa un numero o no
        try:
            opcion = int(opcion)
        except ValueError:
            print("Solamente puedes ingresar numeros")

        # Opcion para sensor DTH11
        if (opcion == 1):
            print("\n Sensor DTH11")
            SensorDHT11()
           

        # Opcion para sensor STH31D
        if (opcion == 2):
            print("\n Sensor STH31D")
            SensorSTH31D()
            

        # Opcion de salida
        if (opcion == 3):
            print("Gracias por usar este programa")
            salir = True


Menu1()
