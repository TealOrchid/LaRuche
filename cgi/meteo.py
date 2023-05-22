#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb

# Connection a la base de donnees
connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="azerty", db="ruche", charset="utf8")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution de la requête MySQL
cursor.execute(f"SELECT thermometrie, hygrometrie, barometrie FROM capteur_meteorologique ORDER BY id DESC LIMIT 1;")

# Récupération des données
donnees = cursor.fetchone()

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close()

# Envoie des données sur le site
print('Content-Type: text/html\n\n')
print(f"""<script>
    document.querySelector('#temperature').innerHTML = '{round(donnees[0], 2)}ºC';
    document.querySelector('#humidite').innerHTML = '{round(donnees[1], 2)}%';
    document.querySelector('#pression').innerHTML = '{round(donnees[2], 2)} hPa';
    </script>""")
