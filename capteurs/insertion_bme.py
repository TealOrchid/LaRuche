#Importations
import bme280
import MySQLdb
import datetime
import time

#Creation des variables
temperature, pression, humidité = bme280.lireBME280Val()[0], bme280.lireBME280Val()[1], bme280.lireBME280Val()[2]
date = str(datetime.datetime.now().date())
heure = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

#Connection a la base de donnees
""""""
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
""""""

# ouvrir cursor
cursor = connection.cursor()#Les curseurs sont créés par la méthode connection.cursor (): ils sont liés à la connexion pendant toute la durée de vie


# Exécuter la requête MySQL
""""""
cursor.execute(f"INSERT INTO `capteur_meteorologique` (`thermometrie`, `hygrometrie`, `barometrie`, `date`, `heure`) VALUES ('{temperature}', '{pression}', '{humidité}', '{date}', '{heure}');")
""""""

# display row count 
connection.commit()#Cette méthode envoie une instruction COMMIT au serveur MySQL, en engageant la transaction en cours

cursor.close()#fermeture cursor
connection.close ()#fermeture connexion

