#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# import MySQLdb module
import MySQLdb

# # Connectez-vous à MySQL en utilisant les paramètres spécifiés (chacun d'eux est facultatif)
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="admin", db="rucheco", charset="utf8")

# ouvrir cursor
cursor = connection.cursor()

# Exécuter la requête MySQL
# Peut utiliser le Format String
# Aussi les paramètres sont utilisées automatiquement par la bibliothèque en utilisant mysql_real_escape_string
# Ou si ce n'est pas supporté par MySQL puis mysql_escape_string
cursor.execute("SELECT * FROM capteur_meteorologique ORDER BY id DESC LIMIT 5")

#for i in range(cursor.rowcount):
    #row=cursor.fetchone()
    #print(row)


#for row in cursor:
    #print(row)
#r = cursor.fetchmany(2)#recupération 2 lignes
#print(r)
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
    else:
        column_string+=column[0]+"       | "   
    i+=1
   
print("\n | "+column_string)
for i in range(cursor.rowcount):
    row=cursor.fetchone()
    print(" | {0} | {1} | {2} | {3} | {4}| ".format(row[0],row[1],row[2],row[3],row[4]))
cursor.close()#fermeture cursor
connection.close #fermeture



    

