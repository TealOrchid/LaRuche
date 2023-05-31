#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, lib_gsm

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT thermometrie, hygrometrie, barometrie FROM capteur_meteorologique ORDER BY id DESC LIMIT 1")

# Récupération des données
row = cursor.fetchone()

# Exécution la requête MySQL
cursor.execute("SELECT numero_telephone FROM contatcs WHERE fonction = 'Apicultrice'")

# Récupération du numéro de téléphone
numero_telephone = cursor.fetchone()

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close()

# Envoie du message
if row[0] <= 10:
    lib_gsm.SendTextMessage(numero_telephone, "La temperature dans la ruche est trop basse !")
    
if row[0] >= 42:
    lib_gsm.SendTextMessage(numero_telephone, "La temperature dans la ruche est trop haute !")
    
if row[1] <= 50:
    lib_gsm.SendTextMessage(numero_telephone, "L'humidite dans la ruche est trop basse !")
    
if row[1] >= 70:
    lib_gsm.SendTextMessage(numero_telephone, "L'humidite dans la ruche est trop elevee !")
    
if row[2] <= 920:
    lib_gsm.SendTextMessage(numero_telephone, "La pression dans la ruche est trop basse !")
