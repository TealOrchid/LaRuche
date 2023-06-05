#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb
from gsmHat import GSMHat

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT poids FROM `capteur_poids` ORDER BY id DESC LIMIT 1")

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

# Init gsmHat
gsm = GSMHat('/dev/ttyAMA0', 115200)

# Envoie du message
if row[0] >= 95:
    gsm.SMS_write(numero_telephone, "Le miel peut etre recolte !")
