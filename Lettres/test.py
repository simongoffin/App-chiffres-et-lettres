#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('dico_u.db')
print "Opened database successfully";
c = conn.cursor()
mot='zebre'
c.execute("SELECT * FROM Mots where Mot like "+"\'"+mot+"\'"+";")
r=c.fetchall()

for i in r:
    print r

conn.commit()
c.close()