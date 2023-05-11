import GPS_ARDUINO
import MySQLdb
import datetime
import time

coordonnees = f"{GPS_ARDUINO.dd_lat}, {GPS_ARDUINO.dd_long}"
print(coordonnees)

date = str(datetime.datetime.now().date())
heure = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

    
""""""
connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
""""""

# ouvrir cursor
cursor = connection.cursor()#Les curseurs sont créés par la méthode connection.cursor (): ils sont liés à la connexion pendant toute la durée de vie


# Exécuter la requête MySQL
""""""
cursor.execute(f"INSERT INTO `gps` (`coordonnees`, `date`, `heure`) VALUES ('{coordonnees}', '{date}', '{heure}');")
""""""

# display row count 
connection.commit()#Cette méthode envoie une instruction COMMIT au serveur MySQL, en engageant la transaction en cours

cursor.close()#fermeture cursor
connection.close ()#fermeture connexion

