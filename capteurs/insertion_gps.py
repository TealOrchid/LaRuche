#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import gps, MySQLdb, datetime

# Creation des variables
gps.init_gps()
tuple_coord = gps.lecture_coordonnees()
coordonnees = f"{tuple_coord[0]}, {tuple_coord[1]}"
date = str(datetime.datetime.now().date())
heure = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

# Connection a la base de donnees
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")

# Ouverture du cursor
cursor = connection.cursor()

# Exécution de la requête MySQL
cursor.execute(f"INSERT INTO `gps` (`coordonnees`, `date`, `heure`) VALUES ('{coordonnees}', '{date}', '{heure}');")

# Envoie d'une instruction COMMIT au serveur MySQL, en engageant la transaction en cours
connection.commit()

# Fermeture cursor
cursor.close()

# Déconnexion de la base de donnees
connection.close()
