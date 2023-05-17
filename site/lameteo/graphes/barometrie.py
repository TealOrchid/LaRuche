#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb

# Connection a la base de donnees
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution de la requête MySQL
cursor.execute(f"SELECT barometrie, date FROM capteur_meteorologique ORDER BY id DESC LIMIT 21;")

donnees = cursor.fetchall()[::-1]
print('Content-Type: text/html\n\n')
for donnee in donnees:
    print(f"<script>valeurs_barometrie.push({donnee[0]});</script>")
    print(f"<script>dates_barometrie.push({donnee[1].strftime('%d/%m')});</script>")

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close
