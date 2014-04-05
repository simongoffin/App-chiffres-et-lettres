#!/usr/bin/python

import sqlite3

f = open('Dictionnaire.txt','r')
lignes  = f.readlines()
f.close()

conn = sqlite3.connect('dico_p.db')
print "Opened database successfully";
c = conn.cursor()
c.execute('''create table Mots(Id integer primary key autoincrement,Mot varchar(9));''')
print "Table created successfully";

for ligne in lignes:
    taille=len(ligne)
    if taille<=9:
        ligne=ligne[0:taille-1]
        print ligne
        c.execute("insert into Mots (Mot) values ("+"\'"+ligne+"\'"+")");
print "Records created successfully";
conn.commit()
c.close()