#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, math
from gsmHat import GSMHat, SMS

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT coordonnees FROM gps ORDER BY id DESC LIMIT 1")

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

# Déclaration des variables
row = row[0].split()
rayon_terre = 6372795.477598
latitude_defaut = 43.113225 * math.pi / 180
longitude_defaut = 5.853035 * math.pi / 180
latitude_actuelle = float(row[0][:-1]) * math.pi / 180
longitude_actuelle = float(row[1]) * math.pi / 180

# Init gsmHat
gsm = GSMHat('/dev/ttyAMA0', 115200)

# Envoie du message
if rayon_terre * math.acos((math.sin(latitude_defaut) * math.sin(latitude_actuelle)) + (math.cos(latitude_defaut) * math.cos(latitude_actuelle) * math.cos(longitude_actuelle - longitude_defaut))) > 1:
    gsm.SMS_write(numero_telephone, "La ruche se fait voler !")
