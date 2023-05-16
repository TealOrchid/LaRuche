#!/usr/bin/env python3
# -*- coding: utf-8 _*

# Import des modules
import time
from smbus import SMBus
bus= SMBus(1)   # 1 indique qu'il faut utiliser le port /dev/i2c-1
Addr7bitsGPS=0x6b # Adresse sur 7 bits=0x60
#Les cavaliers des Pull-up du GPS arduino peuvent rester en place malgré les pull-up du GPIO

#Commande de lecture à partir du registre 0 des 32 Octets de données
data=bus.read_i2c_block_data(Addr7bitsGPS,0)  #adresse 7bits, Offset 0 à partir du 1er registre(registre 1))
# Nombre de registres présents = longeur de la liste)
print('Nbr de registre lus: ',len(data))
# affichage de tous les données contenues dans data
print('data=',data)
# Version du software registre 0 donc offset=0
Version=data[0]
print('La version du Software du CMPS10= ',Version)


data=bus.read_i2c_block_data(Addr7bitsGPS,0)  # Lecture des 32 octets à partir du registre 0 (de 0 à 31)
print("l'heure est :",data[0],data[1],':',data[2],data[3],':',data[4],data[5],"   la date est :",data[6],data[7],'/',data[8],data[9],'/',data[10],data[11],data[12],data[13])
print("La lattitude est :",data[14],data[15],'°',data[16],data[17],',',data[18],data[19],data[20],data[21],"''  La direction est ",chr(data[22]))
Direction=bus.read_byte_data(Addr7bitsGPS,32)  #Lecture d'un seul octet se situant au registre 32. Direction Longitute. Il manquait dans data car il ne va que jusqu'au registre 31
print("La longitude est :",data[23],data[24],data[25],'°',data[26],data[27],',',data[28],data[29],data[30],data[31],"''  La direction est ",chr(Direction))
Sat1=bus.read_byte_data(Addr7bitsGPS,34)
Sat2=bus.read_byte_data(Addr7bitsGPS,35) 
print("Le nombre de satellites détectés est :",Sat1,Sat2,'\n')
degres_lat = data[14] * 10 + data[15]
minutes_lat = data[16] * 10 + data[17] + data[18] * 0.1 + data[19] * 0.01 + data[20] * 0.001 + data[21] * 0.0001
dd_lat = degres_lat + minutes_lat / 60
if chr(data[22]) == "S":
        dd_lat *= -1
degres_long = data[23] * 100 + data[24] * 10 + data[25]
minutes_long = data[26] * 10 + data[27] + data[28] * 0.1 + data[29] * 0.01 + data[30] * 0.001 + data[31] * 0.0001
dd_long = degres_long + minutes_long / 60
if chr(Direction) == "O":
        dd_long *= -1
print("latitude en degres decimal : ", dd_lat)
print("longitude en degres decimal : ", dd_long)



