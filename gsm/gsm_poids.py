#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, lib_gsm

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT poids FROM `capteur_poids` WHERE order by id DESC limit 1")

# Sélection de la dernière ligne de la relation
for i in range(cursor.rowcount):
    row = cursor.fetchone()
    
# Envoie du message
if row[0] >= 95:
    lib_gsm.SendTextMessage("0760291070", "Vous pouvez recolter le miel")

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close
