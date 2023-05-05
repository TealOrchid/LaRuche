#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

#TEST

"""
RECHERCHE au sein de la table capteur_meteorologique
"""


# import MySQLdb module
import MySQLdb

#---------------------------------------------------------------------|
#CONNEXION MYSQL


""""""
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="admin", db="rucheco", charset="utf8")
""""""

# ouvrir cursor
cursor = connection.cursor()


""""""
cursor.execute("SELECT * FROM capteur_meteorologique ORDER BY id DESC LIMIT 5")
""""""


# exécuter row count

print("Totale lignes: {}".format(cursor.rowcount))

#g=cursor.fetchall()#recuperation de l'ensemble tuple
#print(g)
# Obtenir la description de la requête, p.ex. Noms de colonnes, etc.
description = cursor.description

column_string = ""
i=0
# afficher colonnes noms
for column in description:
    if i<2:
        column_string+=column[0]+" | "
    elif i<3:
        column_string+=column[0]+"    | "
    elif i<4:
        column_string+=column[0]+"    | "
    else:
        column_string+=column[0]+"    | "   
    i+=1
   
print("\n | "+column_string)
for i in range(cursor.rowcount):
    row=cursor.fetchone()
    print(" | {0} | {1} | {2} | {3} | {4}| {5}|".format(row[0],row[1],row[2],row[3],row[4], row[5]))
cursor.close()#fermeture cursor
connection.close #fermeture



    

