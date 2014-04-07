
dict_full = open("Dico_full.txt").read().split()
#dic=open("Dictionnaire.txt").read()


mon_fichier = open("mon_dico_full.txt", "w")
for mot in dict_full:
    if len(mot)<11:
        mon_fichier.write(mot+"\n")
mon_fichier.close()




