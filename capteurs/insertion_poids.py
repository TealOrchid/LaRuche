#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""
INSERTION au sein de la table capteur_poids
"""

# Importations
import MySQLdb
import time
import datetime

#---------------------------------------------------------------------|
# Creation des variables

POIDS = 37

V_DATE_now = time.strftime("%Y-%m-%d", time.gmtime())
DATE = ("'"+V_DATE_now+"'")

t=datetime.datetime.now()

V_HEURE_now = time.strftime(f"{t.hour}:%M:%S", time.gmtime())
HEURE = ("'"+V_HEURE_now+"'")



#---------------------------------------------------------------------|
#CONNEXION MYSQL

""""""
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="admin", db="rucheco", charset="utf8")
""""""

# Ouverture du cursor
cursor = connection.cursor()#Les curseurs sont créés par la méthode connection.cursor (): ils sont liés à la connexion pendant toute la durée de vie


# Exécution la requête MySQL
""""""
cursor.execute(f"INSERT INTO `capteur_poids` (`poids`, `date`, `heure`) VALUES ('{POIDS}', '{V_DATE_now}', '{V_HEURE_now}');")
""""""

# display row count 
connection.commit()# Envoie d'une instruction COMMIT au serveur MySQL, en engageant la transaction en cours

cursor.close()#fermeture cursor
connection.close ()#fermeture connexion
