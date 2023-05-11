#!/usr/bin/python3

#--------------------------------------
import smbus
import time
from ctypes import c_short
from ctypes import c_byte


DEVICE = 0x77 # Adresse I2C de l'appareil par défaut


bus = smbus.SMBus(1) # Rev  Pi 3 & Pi 4 utilise le bus 1
                     

def getShort(data, index):
  # renvoie deux octets de données sous forme de valeur 16 bits signée
  return c_short((data[index+1] << 8) + data[index]).value

def getUShort(data, index):
  # renvoie deux octets de données sous la forme d'une valeur 16 bits non signée
  return (data[index+1] << 8) + data[index]

def getChar(data,index):
  # renvoie un octet des données sous forme de caractère signé
  return c_byte(data[index]).value
 

def getUChar(data,index):
  # renvoie un octet à partir des données sous la forme d'un caractère non signé
  result =  data[index] & 0xFF
  return result

def lireBME280ID(addr=DEVICE):
  # Chip ID Registre Adresse
  REG_ID     = 0xD0
  (chip_id, chip_version) = bus.read_i2c_block_data(addr, REG_ID, 2)
  return (chip_id, chip_version)

def lireBME280Val(addr=DEVICE):
  # Registre Adresses BME280
  REG_DATA = 0xF7
  REG_CONTROL = 0xF4
  REG_CONFIG  = 0xF5

  REG_CONTROL_HUM = 0xF2
  REG_HUM_MSB = 0xFD
  REG_HUM_LSB = 0xFE

  # Paramètre de suréchantillonnage - page 27
  OVERSAMPLE_TEMP = 2
  OVERSAMPLE_PRES = 2
  MODE = 1

  # Paramètre de suréchantillonnage de registre humidité - page 26
  OVERSAMPLE_HUM = 2
  bus.write_byte_data(addr, REG_CONTROL_HUM, OVERSAMPLE_HUM)

  control = OVERSAMPLE_TEMP<<5 | OVERSAMPLE_PRES<<2 | MODE
  bus.write_byte_data(addr, REG_CONTROL, control)

  # Lire des blocs de données d'étalonnage à partir de EEPROM
  # voir Page 22 data sheet
  cal1 = bus.read_i2c_block_data(addr, 0x88, 24)
  cal2 = bus.read_i2c_block_data(addr, 0xA1, 1)
  cal3 = bus.read_i2c_block_data(addr, 0xE1, 7)

  # Convertir des données d'octet en valeurs de mot
  dig_T1 = getUShort(cal1, 0)
  dig_T2 = getShort(cal1, 2)
  dig_T3 = getShort(cal1, 4)

  dig_P1 = getUShort(cal1, 6)
  dig_P2 = getShort(cal1, 8)
  dig_P3 = getShort(cal1, 10)
  dig_P4 = getShort(cal1, 12)
  dig_P5 = getShort(cal1, 14)
  dig_P6 = getShort(cal1, 16)
  dig_P7 = getShort(cal1, 18)
  dig_P8 = getShort(cal1, 20)
  dig_P9 = getShort(cal1, 22)

  dig_H1 = getUChar(cal2, 0)
  dig_H2 = getShort(cal3, 0)
  dig_H3 = getUChar(cal3, 2)

  dig_H4 = getChar(cal3, 3)
  dig_H4 = (dig_H4 << 24) >> 20
  dig_H4 = dig_H4 | (getChar(cal3, 4) & 0x0F)

  dig_H5 = getChar(cal3, 5)
  dig_H5 = (dig_H5 << 24) >> 20
  dig_H5 = dig_H5 | (getUChar(cal3, 4) >> 4 & 0x0F)

  dig_H6 = getChar(cal3, 6)

  # Attente en ms (Fiche technique Annexe B page 51: Temps de mesure et calcul du courant)
  wait_time = 1.25 + (2.3 * OVERSAMPLE_TEMP) + ((2.3 * OVERSAMPLE_PRES) + 0.575) + ((2.3 * OVERSAMPLE_HUM)+0.575)
  time.sleep(wait_time/1000)  #Attendre le temps requis 

  # Lire température/pression/humidité
  data = bus.read_i2c_block_data(addr, REG_DATA, 8)
  pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
  temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
  hum_raw = (data[6] << 8) | data[7]

  #Affiner température
  var1 = ((((temp_raw>>3)-(dig_T1<<1)))*(dig_T2)) >> 11
  var2 = (((((temp_raw>>4) - (dig_T1)) * ((temp_raw>>4) - (dig_T1))) >> 12) * (dig_T3)) >> 14
  t_fine = var1+var2
  temperature = float(((t_fine * 5) + 128) >> 8);

  # Affiner pression et ajuster à la température
  var1 = t_fine / 2.0 - 64000.0
  var2 = var1 * var1 * dig_P6 / 32768.0
  var2 = var2 + var1 * dig_P5 * 2.0
  var2 = var2 / 4.0 + dig_P4 * 65536.0
  var1 = (dig_P3 * var1 * var1 / 524288.0 + dig_P2 * var1) / 524288.0
  var1 = (1.0 + var1 / 32768.0) * dig_P1
  if var1 == 0:
    pression=0
  else:
    pression = 1048576.0 - pres_raw
    pression = ((pression - var2 / 4096.0) * 6250.0) / var1
    var1 = dig_P9 * pression * pression / 2147483648.0
    var2 = pression * dig_P8 / 32768.0
    pression = pression + (var1 + var2 + dig_P7) / 16.0

  # Affiner humidité
  humidite = t_fine - 76800.0
  humidite = (hum_raw - (dig_H4 * 64.0 + dig_H5 / 16384.0 * humidite)) * (dig_H2 / 65536.0 * (1.0 + dig_H6 / 67108864.0 * humidite * (1.0 + dig_H3 / 67108864.0 * humidite)))
  humidite = humidite * (1.0 - dig_H1 * humidite / 524288.0)
  if humidite > 100:
    humidite = 100
  elif humidite < 0:
    humidite = 0

  return temperature/100.0,pression/100.0,humidite

def version_bme280():

  (chip_id, chip_version) = lireBME280ID()
  print ("Composant ID :", chip_id)
  print ("Version :", chip_version)

def bme280():
  temperature,pression,humidite = lireBME280Val()

  print ("Température : ", temperature, "°C")
  print ("Pression : ", round (pression,2), "hPa")
  print ("Humidité : ", round(humidite,2), "%")
  print("____________________________")

if __name__=="__main__":
  version_bme280()
  while True:
    bme280()
    time.sleep(3)
