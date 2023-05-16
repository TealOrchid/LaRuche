#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Import des modules
from smbus import SMBus

# Déclaration des variables
bus = SMBus(1) # 1 indique qu'il faut utiliser le port /dev/i2c-1
Addr7bitsGPS=0x6b # Adresse sur 7 bits=0x60
data = bus.read_i2c_block_data(Addr7bitsGPS,0) # Lecture des 32 octets à partir du registre 0 (de 0 à 31)
Direction = bus.read_byte_data(Addr7bitsGPS,32) # Lecture d'un seul octet se situant au registre 32. Direction Longitute. Il manquait dans data car il ne va que jusqu'au registre 31

# Latitude
degres_lat = data[14] * 10 + data[15]
minutes_lat = data[16] * 10 + data[17] + data[18] * 0.1 + data[19] * 0.01 + data[20] * 0.001 + data[21] * 0.0001
dd_lat = degres_lat + minutes_lat / 60
if chr(data[22]) == "S":
    dd_lat *= -1

# Longitude
degres_long = data[23] * 100 + data[24] * 10 + data[25]
minutes_long = data[26] * 10 + data[27] + data[28] * 0.1 + data[29] * 0.01 + data[30] * 0.001 + data[31] * 0.0001
dd_long = degres_long + minutes_long / 60
if chr(Direction) == "O":
    dd_long *= -1
