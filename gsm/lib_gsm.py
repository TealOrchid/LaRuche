#!/usr/bin/env python3
#_*_coding:Utf-8_*_

import RPi.GPIO as GPIO
import serial
import time, sys
import datetime

P_BUTTON = 15 # Button, gpio 15
RESET_gsm = 24 #sortie reset
GPIO.setwarnings(False)

SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 3
#SERIAL_PORT = "/dev/ttyS0"    # Raspberry Pi 2

ser = serial.Serial(
    SERIAL_PORT,
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 3)
    # Attention le timeout défini dans l'objet ser doit être assez grand 3s ou plus
    # pour que les commandes "readlines" puissent tout récupérer
    # Attention les readline s'arrête sur \n alors que readlines avec le timeout (vaut mieux ce dernier)
    # Paramétrage du format des messages utilisés dans les commandes d'envoi, reception, lecture et écriture (doc page 201)

def setup(RESET_gsm=26):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RESET_gsm, GPIO.OUT)
    GPIO.output(RESET_gsm,0)
    #RESET GSM Pendant 200 ms 0 puis 1
    print('mise à 0')
    time.sleep(0.2)
    print('mise à 1\n')
    GPIO.output(RESET_gsm,1)
    time.sleep(0.5)

def Initialize():
    ser.write(b'AT+CMGF=1\r') # commande at: la valeur 1 correspond au "text mode" voir tuto page 12 et 16 de philippe
    reponse=ser.readlines() #readlines permet d'avoir l'ensemble des éléments de la réponse (ne pas prendre readline)
    print('init=',reponse)
    while(reponse!=[b'AT+CMGF=1\r\r\n', b'OK\r\n']): # 1ere possibilité on teste l'ensemble des éléments de la liste(voir 2eme possibilité ci-dessous)
        ser.write(b'AT+CMGF=1\r')
        reponse=ser.readlines()
        print('init=',reponse)
        time.sleep(0.5)
    print('init GSM OK\n')
    time.sleep(0.5)
# Reset du GSM
#print('reset')
#setup()

def CheckNetworkStatus():
    #Etat du Réseau (Pas utile la commande AT de la DEL suffit)
    ser.write(b'AT+CREG=?\r') # Demande Etat Reseau (doc page 100 et 99)
    reponse=ser.readlines()
    print('EtatReseau=',reponse)

    #Del Etat du Reseau
    ser.write(b'AT#SLED=2\r') # Activation de la Del Etat du RESEAU (doc page 290)
    reponse=ser.readlines()
    print('LED_Reseau=',reponse)
    while(b'OK\r\n' not in reponse):  # 2eme possibilité de test avec not in, on se limite à l'élement contenant le OK avec les caractères de contrôle
        ser.write(b'AT#SLED=2\r')
        reponse=ser.readlines()
        print('LED_Reseau=',reponse)
        time.sleep(0.5)
    print('Reseau OK\n')
    time.sleep(0.5)

def SendTextMessage(numero,message):
    nu='AT+CMGS="'+numero+'"\r'
    nu=nu.encode()
    ser.write(nu)
    reponse=ser.readlines()
    print('NumTEL=',reponse)
    time.sleep(1)
    msgencod=message.encode('ascii')
    ser.write(msgencod +  bytes([26])) # le caractère ascii 26 (CTRL+Z) est obligatoire pour finir l'envoi (doc page 244)
    # Attention le timeout défini dans l'objet ser doit être assez grand 3s
    # pour que le readlines puisse tout récupérer car l'envoi du SMS est plus
    # long que les autres  commandes AT précédentes
    reponse=ser.readlines()
    return reponse

if __name__=="__main__":
    print('reset')
    setup()
    Initialize()
    CheckNetworkStatus()
    rep=SendTextMessage("0760291070","bonjour")
    print('EnvoiSMS=',rep,'\n')
