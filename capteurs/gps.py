#!/usr/bin/python3
# -*- coding:UTF-8 -*-

# Importations
import serial, time
import RPi.GPIO as GPIO

# Choisir le connecteur GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def init_gps():
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    time.sleep(4)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(7, GPIO.LOW)
    time.sleep(5)

# Ouverture du port serie
setup = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 115200,  # vitesse 115200 bauds
    parity = serial.PARITY_NONE,  # pas de parité
    stopbits = serial.STOPBITS_ONE,  # un stop bit
    bytesize = serial.EIGHTBITS,  # format 8 bits
    timeout = 3)  # timeout 100 ms

# Commentaire
reponse = []
while (reponse != [b'AT+CGNSPWR=1\r\r\n', b'OK\r\n']):
    setup.write(b'AT+CGNSPWR=1\r\n')
    reponse = setup.readlines()
    print(reponse)
    if reponse == []:
        init_gps()

# Déclaration des variables            
setup.write(b"AT+CGNSINF\r\n")
reponse = setup.readlines()
coordonnees = reponse[1].decode().split(',')
latitude = coordonnees[3]
longitude = coordonnees[4]
altitude = coordonnees[5]

# Prints de contrôle
print(reponse,"Données GPS")
print(coordonnees)
print(f"Latitude : {latitude}°")
print(f"Longitude : {longitude}°")
print(f"Altitude : {altitude}m")

# Fermeture du port serie
setup.close()
