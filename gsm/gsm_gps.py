#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb, lib_gsm

# Connection à MySQL
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution la requête MySQL
cursor.execute("SELECT coordonnees FROM gps order by id DESC limit 1")


# Obtention de la description de la requête MySQL
description = cursor.description

# Affichage des colonnes
column_string = ""
i = 0

for column in description:
    if i < 2:
        column_string += column[0] + " | "
    elif i < 3:
        column_string += column[0] + "    | "
    else:
        column_string += column[0] + "       | "   
    i += 1

print("\n | "+column_string)

for i in range(cursor.rowcount):
    row=(cursor.fetchone())
    print(" | {0} |".format(row[0]))

# Envoie du message
if row[0][0] >= "valeur" or row[0][0] <= "valeur" or row[0][1] >= "valeur" or row[0][1] <= "valeur":
    rep=lib_gsm.SendTextMessage("0760291070","La ruche se fait voler !!!")
    print('EnvoiSMS=',rep,'\n')

# Fermeture du cursor 
cursor.close()

# Déconnection de MySQL
connection.close
