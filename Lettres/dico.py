dict = open("mon_dico_full_a.txt").read().split()
dict_full=open("mon_dico_full.txt").read().split()
dic=open("mon_dico_full_a.txt").read()


box={}
index=0
for mot in dict:
    box[mot]=index
    index+=1