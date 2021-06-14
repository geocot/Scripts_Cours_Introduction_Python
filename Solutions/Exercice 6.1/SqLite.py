import sqlite3

fichierDonnees =r"c:\temp\demo2.db3"
conn =sqlite3.connect(fichierDonnees)
cur =conn.cursor()

#cur.execute("CREATE TABLE membres3 (age INTEGER, nom TEXT, taille REAL)")
#cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
#cur.execute("DELETE FROM membres WHERE nom='Dupont'")
lignes = cur.execute("SELECT * FROM membres")
for l in lignes:
    print(l)
#conn.commit()
cur.close()