#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# Importations
import MySQLdb

connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")

# Récuperation de la température
def temperature() -> float:
    """
    Renvoie la dernière valeur de l'attribut thermometrie de la table capteur_meteorologique

    :return: dernière température mesuré
    :rtype: float
    """
    cursor = connection.cursor()
    cursor.execute("SELECT thermometrie FROM capteur_meteorologique ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    cursor.close()
    connection.close
    return row[0]

# Récuperation de la pression
def pression() -> float:
    """
    Renvoie la dernière valeur de l'attribut barometrie de la table capteur_meteorologique

    :return: dernière pression mesuré
    :rtype: float
    """
    cursor = connection.cursor()
    cursor.execute("SELECT barometrie FROM capteur_meteorologique ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    cursor.close()
    connection.close
    return row[0]

# Récuperation de l'humidité
def humidite() -> float:
    """
    Renvoie la dernière valeur de l'attribut hygrometrie de la table capteur_meteorologique

    :return: dernier taux d'humidité mesuré
    :rtype: float
    """
    cursor = connection.cursor()
    cursor.execute("SELECT hygrometrie FROM capteur_meteorologique ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    cursor.close()
    connection.close
    return row[0]

# Récuperation du poids
def poids() -> float:
    """
    Renvoie la dernière valeur de l'attribut poids de la table capteur_poids

    :return: dernier poids mesuré
    :rtype: float
    """
    cursor = connection.cursor()
    cursor.execute("SELECT poids FROM capteur_poids ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    cursor.close()
    connection.close
    return row[0]

# Récuperation des coordonnées
def coordonnees() -> tuple:
    """
    Renvoie la dernière valeur de l'attribut coordonnees de la table gps

    :return: dernières coordonnées mesuré
    :rtype: tuple
    """
    cursor = connection.cursor()
    cursor.execute("SELECT coordonnees FROM gps ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    cursor.close()
    connection.close
    return row[0]
