#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import serial
import time


class GPS:
    @staticmethod
    def __GPIOSetup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, GPIO.LOW)
        time.sleep(4)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(7, GPIO.LOW)
        time.sleep(5)

    def __init__(self, port, baudrate):
        self.__port = port
        self.__baudrate = baudrate
        self.__ser = serial.Serial(
            port=self.__port,
            baudrate=self.__baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=3)
        self.__connect()
        self.GNSS_status = 0
        self.Fix_status = 0
        self.UTC = ''
        self.Latitude = 0.0
        self.Longitude = 0.0
        self.Altitude = 0.0
        self.Speed = 0.0
        self.Course = 0.0
        self.HDOP = 0.0
        self.PDOP = 0.0
        self.VDOP = 0.0
        self.GPS_satellites = 0
        self.GNSS_satellites = 0
        self.Signal = 0.0
        self.__get_coordinates()

    def __connect(self):
        data = []
        while (data != [b'AT+CGNSPWR=1\r\r\n', b'OK\r\n']):
            self.__ser.write(b'AT+CGNSPWR=1\r\n')
            data = self.__ser.readlines()
            print(data)
            if not data:
                self.__GPIOSetup()

    def __get_coordinates(self):
        self.__ser.write(b"AT+CGNSINF\r\n")
        rawData = self.__ser.readlines()
        data = rawData[1].decode().split(',')
        self.GNSS_status = data[0]
        self.Fix_status = data[1]
        self.UTC = data[2]
        self.Latitude = data[3]
        self.Longitude = data[4]
        self.Altitude = data[5]
        self.Speed = data[6]
        self.Course = data[7]
        self.HDOP = data[10]
        self.PDOP = data[11]
        self.VDOP = data[12]
        self.GPS_satellites = data[14]
        self.GNSS_satellites = data[15]
        self.Signal = data[18]

    def close(self):
        self.__ser.close()
