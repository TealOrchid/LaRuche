#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, lib_gsm

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT poids FROM `capteur_poids` ORDER BY id DESC LIMIT 1")

# Récupération des données
row = cursor.fetchone()

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close()

# Envoie du message
if row[0] >= 95:
    lib_gsm.SendTextMessage("0760291070", "Vous pouvez recolter le miel")
