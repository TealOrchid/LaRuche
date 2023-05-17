#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, lib_gsm

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT thermometrie, hygrometrie, barometrie FROM capteur_meteorologique WHERE order by id DESC limit 1")

# Sélection de la dernière ligne de la relation
row = cursor.fetchone()

# Envoie du message
if row[0] <= 15:
    lib_gsm.SendTextMessage("0760291070", "Température dans la ruche trop basse !")
    
if row[0] >= 40:
    lib_gsm.SendTextMessage("0760291070", "Température dans la ruche trop haute !")
    
if row[1] <= "valeur":
    lib_gsm.SendTextMessage("0760291070", "Humidité dans la ruche trop basse !")
    
if row[1] >= "valeur":
    lib_gsm.SendTextMessage("0760291070", "Humidité dans la ruche trop élevée !")
    
if row[2] <= "valeur":
    lib_gsm.SendTextMessage("0760291070", "Pression dans la ruche trop basse !")
    
if row[2] >= "valeur":
    lib_gsm.SendTextMessage("0760291070", "Pression dans la ruche trop élevée !")

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close
