#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, datetime
from hx711 import HX711

# Creation des variables
brocheDT = 11   # DT du HX711 branché à GPIO5
brocheSCK = 12  # SCK du HX711 branché à GPIO6
hx = HX711(brocheDT, brocheSCK) 
poids = hx.get_weight(5)
date = str(datetime.datetime.now().date())
heure = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

# Connection a la base de donnees
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution de la requête MySQL
cursor.execute(f"INSERT INTO `capteur_poids` (`poids`, `date`, `heure`) VALUES ('{poids}', '{date}', '{heure}');")

# Envoie d'une instruction COMMIT au serveur MySQL, en engageant la transaction en cours
connection.commit()

# Fermeture cursor
cursor.close()

# Déconnexion de la base de donnees
connection.close()
