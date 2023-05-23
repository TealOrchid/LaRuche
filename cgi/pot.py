#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb

# Connection a la base de donnees
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution de la requête MySQL
cursor.execute(f"SELECT poids FROM capteur_poids ORDER BY id DESC LIMIT 1;")

# Récupération des données
poids = cursor.fetchone()[0]

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close()

# Traitement des données
poids_max = 100
pourcentage = poids * 100 / poids_max
pourcentage = "0" + str(pourcentage) if pourcentage < 10 else str(pourcentage)

# Envoie des données sur le site
print('Content-Type: text/html\n\n')
if float(pourcentage) < 100:
    print(f"<img src='images/pots/pot{pourcentage[0]}.png' alt='Pot de miel'>")
else:
    print(f"<img src='images/pots/pot10.png' alt='Pot de miel'>")
