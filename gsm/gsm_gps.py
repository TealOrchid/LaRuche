#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# import MySQLdb module
import MySQLdb
import lib_gsm

# # Connectez-vous à MySQL en utilisant les paramètres spécifiés (chacun d'eux est facultatif)
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8mb4")

# ouvrir cursor
cursor = connection.cursor()

# Exécuter la requête MySQL
# Peut utiliser le Format String
# Aussi les paramètres sont utilisées automatiquement par la bibliothèque en utilisant mysql_real_escape_string
# Ou si ce n'est pas supporté par MySQL puis mysql_escape_string
cursor.execute("SELECT coordonnees FROM gps WHERE heure = (select max(heure) from gps) and date = (select max(date) from gps)")

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
    row=(cursor.fetchone())
    print(" | {0} |".format(row[0]))
    
#envoie du message
if row[0][0] >= "valeur" or row[0][0] <= "valeur" or row[0][1] >= "valeur" row[0][1] <= "valeur":
    #lib_gsm.setup()
    #lib_gsm.Initialize()
    #lib_gsm.CheckNetworkStatus()
    rep=lib_gsm.SendTextMessage("0760291070","La ruche se fait voler !!!")
    print('EnvoiSMS=',rep,'\n')
    
cursor.close()#fermeture cursor
connection.close #fermeture


    






