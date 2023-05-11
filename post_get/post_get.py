#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

#importation
import MySQLdb

#récuperation de la temperature
def temperature():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT thermometrie FROM capteur_meteorologique order by id desc limit 1")
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

##récuperation de la pression
def pression():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT barometrie FROM capteur_meteorologique order by id desc limit 1")
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

#récuperation de l'humidite
def humidite():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT hygrometrie FROM capteur_meteorologique order by id desc limit 1")
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

#recuperation du poids
def poids():
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT poids FROM `capteur_poids` order by id DESC limit 1")
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
