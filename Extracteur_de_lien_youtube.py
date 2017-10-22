# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:11:04 2017

@author: JulienA
"""

"""Ce programme à pour objectif de choper tous les liens youtube d'une 
                            page facebook """

""" Etape 1: Choper le code source de la page qui nous intéresse
    Etape 2: Copier ce code source dans un fichier texte
    Etape 3: Repérer les liens youtube dans ces fichiers
    Etape 4: Traduire ces liens "criptés" en liens utilisables
    Etapes 5: Les copier dans un autre fichier txt """

#Etape 1, 2 faits dans le fichier "DLC.txt"

f = open("Nouveau document texte.txt", "r") # <-- Doc .txt copie de la page HTML d'origine
q = open("Decodage.txt", "a") # <-- Doc .txt où on met les liens décriptés
chaine = "https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D" # <-- Chaine de caractère qu'il y a en commun à chaque lien youtube


text = []
tab = []
tab2 = []
tab3 = []

# Remplie un tableau (tab) où je j'ai la position de "chaine" dans le texte
# tab renvoie -1 si chaine pas présent dans la ligne et n qui est la nième position de la chaine dans le texte
# tab[l] correspond à la lième ligne

for lines in f.readlines():
    u = lines.find(chaine)
    tab.append(u)
print(tab)     

f.close()

#Remplie deux tableaux: tab2 et tab3 qui nous informe de la position en ligne (tab2) et la position en colonne (tab3)
for i in range(len(tab)):
    if tab[i] != -1:
        tab2.append(i) #ligne
        tab3.append(tab[i]) #position caractère
print(tab2)
print(tab3)


f = open("Test.txt", "r")

#Le nerf de la guerre ;)
#Ici on remplie un tableau qui prend seulement les lignes ou on a le lien qui est présent


for i,line in enumerate(f):
    for c in range(len(tab3)):
        if i in tab2:
            for j, carac in enumerate(line):
                if j >= tab3[c] and j <= tab3[c] + 56:
                    print(j)
                    print(carac)
                    text.append(carac)
            text.append("\n")

for i in range(len(tab3)):
    print(tab3[i])
    
u = "".join(text)
u=u.replace("%3A", ":")
u=u.replace("%2F", "/")
u=u.replace("%3F", "?")
u=u.replace("%3D", "=")
print(u)

q.write(u)




q.close()
f.close()














