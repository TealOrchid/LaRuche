#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb

# Connection a la base de donnees
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution de la requête MySQL
cursor.execute(f"SELECT hygrometrie, date FROM capteur_meteorologique ORDER BY id DESC LIMIT 7;")

# Récupération des données
donnees = cursor.fetchall()[::-1]

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close()

# Envoie des données sur le site
print('Content-Type: text/html\n\n')
print(f"""<script>
    let valeurs = {[donnee[0] for donnee in donnees]};
    let dates = {[donnee[1].strftime('%d/%m') for donnee in donnees]};
    </script>""")
