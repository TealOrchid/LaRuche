import shutil, time, MySQLdb, post_get

#shutil.move('/media/pi/CL/Projet_ruche_2023/mes_tests/dossier1/fichier', '/media/pi/CL/Projet_ruche_2023/mes_tests/dossier2/fichier2')

temps = time.time()
donnee = post_get.poids()
nom = post_get.pot()


if donnee < "24":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot0%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot0%.png', '/LaRuche-main/site/images/pot.png')

if donnee >= "24" and donnee < "28":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot10%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot10%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "28" and donnee < "32":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot20%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot20%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "32" and donnee < "36":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot30%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot30%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "36" and donnee < "40":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot40%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot40%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "40" and donnee < "44":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot50%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot50%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "44" and donnee < "48":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot60%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot60%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "48" and donnee < "52":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot70%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot70%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "56" and donnee < "58":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot80%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot80%.png', '/LaRuche-main/site/images/pot.png')
    
if donnee >= "58" and donnee <"60":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot90%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot90%.png', '/LaRuche-main/site/images/pot.png')

if donnee >= "60":
    connection = MySQLdb.connect(host="localhost", port=3306, user="admin", passwd="Miel", db="ruche", charset="utf8")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO pot (id, nom) VALUES ({temps}, 'pot100%')")
    cursor.close()#fermeture cursor
    connection.close #fermeture
    shutil.move('/LaRuche-main/site/images/pot.png', f'/LaRuche-main/site/pots/{nom}.png')
    shutil.move('/LaRuche-main/site/pots/pot90%.png', '/LaRuche-main/site/images/pot.png')

