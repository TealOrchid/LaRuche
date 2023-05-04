#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, lib_gsm

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT thermometrie, hygrometrie, barometrie FROM capteur_meteorologique WHERE date = (select max(date) from capteur_meteorologique) order by heure desc limit 1")

# Obtention de la description de la requête MySQL
description = cursor.description

# Affichage des colonnes
column_string = ""
i = 0

for column in description:
    if i < 2:
        column_string += column[0] + " | "
    elif i < 3:
        column_string += column[0] + "    | "
    else:
        column_string += column[0] + "       | "   
    i += 1

print("\n | " + column_string)

for i in range(cursor.rowcount):
    row = cursor.fetchone()
    print(" | {0} | {1} | {2} |".format(row[0], row[1], row[2]))

# Envoie du message
if row[0] <= 15:
    rep = lib_gsm.SendTextMessage("0760291070", "Température dans la ruche trop basse !")
    print('EnvoiSMS=', rep, '\n')
    
if row[0] >= 40:
    rep = lib_gsm.SendTextMessage("0760291070", "Température dans la ruche trop haute !")
    print('EnvoiSMS=', rep, '\n')
    
if row[1] <= "valeur":
    rep = lib_gsm.SendTextMessage("0760291070", "Humidité dans la ruche trop basse !")
    print('EnvoiSMS=', rep, '\n')
    
if row[1] >= "valeur":
    rep = lib_gsm.SendTextMessage("0760291070", "Humidité dans la ruche trop élevée !")
    print('EnvoiSMS=', rep, '\n')
    
if row[2] <= "valeur":
    rep = lib_gsm.SendTextMessage("0760291070", "Pression dans la ruche trop basse !")
    print('EnvoiSMS=', rep, '\n')
    
if row[2] >= "valeur":
    rep = lib_gsm.SendTextMessage("0760291070", "Pression dans la ruche trop élevée !")
    print('EnvoiSMS=', rep, '\n')

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close
