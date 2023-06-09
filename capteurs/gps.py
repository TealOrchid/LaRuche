#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import serial, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def init_GPIO():
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    time.sleep(4)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(7, GPIO.LOW)
    time.sleep(5)

setup = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 115200,  # vitesse 115200 bauds
    parity = serial.PARITY_NONE,  # pas de parité
    stopbits = serial.STOPBITS_ONE,  # un stop bit
    bytesize = serial.EIGHTBITS,  # format 8 bits
    timeout = 3)  # timeout 100 ms

def init_gps():
    reponse = []
    while (reponse != [b'AT+CGNSPWR=1\r\r\n', b'OK\r\n']):
        setup.write(b'AT+CGNSPWR=1\r\n')
        reponse = setup.readlines()
        if reponse == []:
            init_GPIO()

def lecture_coordonnees():         
    setup.write(b"AT+CGNSINF\r\n")
    reponse = setup.readlines()
    coordonnees = reponse[1].decode().split(',')
    return coordonnees[3], coordonnees[4]
