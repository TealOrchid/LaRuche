#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb

# Connection a la base de donnees
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution de la requête MySQL
cursor.execute(f"SELECT coordonnees FROM gps ORDER BY id DESC LIMIT 1;")

# Récupération des données
donnees = cursor.fetchone()

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close()

# Traitement des données
donnees = donnees[0].split()

# Envoie des données sur le site
print('Content-Type: text/html\n\n')
print(f"""<script>
    let latitude = {donnees[0][:-2]};
    let longitude = {donnees[1]};
    </script>""")
