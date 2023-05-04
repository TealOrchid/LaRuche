import MySQLdb

def temperature():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT thermometrie FROM capteur_meteorologique WHERE date = (select max(date) from capteur_meteorologique) order by heure desc limit 1")
    description = cursor.description
    i = 0
    column_string = ""
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
        print(" | {0} | ".format(row[0]))
    return row[0]
    cursor.close()#fermeture cursor
    connection.close #fermeture


def pression():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT barometrie FROM capteur_meteorologique WHERE date = (select max(date) from capteur_meteorologique) order by heure desc limit 1")
    description = cursor.description
    i = 0
    column_string = ""
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
        print(" | {0} | ".format(row[0]))
    return row[0]
    cursor.close()#fermeture cursor
    connection.close #fermeture

def humidite():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT hygrometrie FROM capteur_meteorologique WHERE date = (select max(date) from capteur_meteorologique) order by heure desc limit 1")
    description = cursor.description
    i = 0
    column_string = ""
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
        print(" | {0} | ".format(row[0]))
    return row[0]
    cursor.close()#fermeture cursor
    connection.close #fermeture

def poids():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT poids FROM `capteur_poids` where date = (select max(date) from capteur_poids) order by heure DESC limit 1")
    description = cursor.description
    i = 0
    column_string = ""
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
        print(" | {0} | ".format(row[0]))
    return row[0]
    cursor.close()#fermeture cursor
    connection.close #fermeture
    
def pot():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT nom FROM pot WHERE id = (select max(id) from pot)")
    description = cursor.description
    i = 0
    column_string = ""
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
        print(" | {0} | ".format(row[0]))
    return row[0]
    cursor.close()#fermeture cursor
    connection.close #fermeture
