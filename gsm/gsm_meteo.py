#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb
from gsmHat import GSMHat, SMS

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT thermometrie, hygrometrie, barometrie FROM capteur_meteorologique ORDER BY id DESC LIMIT 1")

# Récupération des données
row = cursor.fetchone()

# Exécution la requête MySQL
cursor.execute("SELECT numero_telephone FROM contacts WHERE fonction = 'Apicultrice'")

# Récupération du numéro de téléphone
numero_telephone = cursor.fetchone()[0]

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close()

# Init gsmHat
gsm = GSMHat('/dev/ttyAMA0', 115200)

# Envoie du message
if row[0] <= 10:
    gsm.SMS_write(numero_telephone, "La temperature dans la ruche est trop basse !")
    
if row[0] >= 42:
    gsm.SMS_write(numero_telephone, "La temperature dans la ruche est trop haute !")
    
if row[1] <= 50:
    gsm.SMS_write(numero_telephone, "L'humidite dans la ruche est trop basse !")
    
if row[1] >= 70:
    gsm.SMS_write(numero_telephone, "L'humidite dans la ruche est trop elevee !")
    
if row[2] <= 920:
    gsm.SMS_write(numero_telephone, "La pression dans la ruche est trop basse !")