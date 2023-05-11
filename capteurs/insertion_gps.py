#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import GPS_ARDUINO
import MySQLdb
import datetime
import time

# Creation des variables
coordonnees = f"{GPS_ARDUINO.dd_lat}, {GPS_ARDUINO.dd_long}"
date = str(datetime.datetime.now().date())
heure = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

# Connection a la base de donnees 
""""""
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
""""""

# Overture du cursor
cursor = connection.cursor()#Les curseurs sont créés par la méthode connection.cursor (): ils sont liés à la connexion pendant toute la durée de vie


# Exécution de la requête MySQL
""""""
cursor.execute(f"INSERT INTO `gps` (`coordonnees`, `date`, `heure`) VALUES ('{coordonnees}', '{date}', '{heure}');")
""""""

# display row count 
connection.commit()#Envoie d'une instruction COMMIT au serveur MySQL, en engageant la transaction en cours

cursor.close()#fermeture cursor
connection.close ()#fermeture connexion

