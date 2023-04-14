#TEST

"""
INSERTION au sein de la table CAPTEUR_POIDS
"""

#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# import MySQLdb module
import MySQLdb
import time
import datetime

#---------------------------------------------------------------------|

""""""
POIDS = 37

""""""


""""""
V_DATE_now = time.strftime("%Y-%m-%d", time.gmtime())
DATE = ("'"+V_DATE_now+"'")

t=datetime.datetime.now()

V_HEURE_now = time.strftime(f"{t.hour}:%M:%S", time.gmtime())
HEURE = ("'"+V_HEURE_now+"'")
""""""
print(DATE, HEURE)


#---------------------------------------------------------------------|
#CONNEXION MYSQL

""""""
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="admin", db="rucheco", charset="utf8")
""""""

# ouvrir cursor
cursor = connection.cursor()#Les curseurs sont créés par la méthode connection.cursor (): ils sont liés à la connexion pendant toute la durée de vie


# Exécuter la requête MySQL
""""""
cursor.execute(f"INSERT INTO `capteur_poids` (`poids`, `date`, `heure`) VALUES ('{POIDS}', '{V_DATE_now}', '{V_HEURE_now}');")
""""""

# display row count 
connection.commit()#Cette méthode envoie une instruction COMMIT au serveur MySQL, en engageant la transaction en cours

cursor.close()#fermeture cursor
connection.close ()#fermeture connexion
