# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:57:41 2022

@author: By237Fact
"""
# Manipulation basique des tuples

# t1 = (2,6,8,4)

# print(len(t1))
# t1[1]

# print(t1[-2:])

# # erreur car les tuples sont en lecture seule
# # t1[-1] = 10

# print(t1*2)

# # tuples d'objets hétérogènes
# t2 = (3.6,"Toto",True,t1,34.1)
# print(t2)

# # tuples de tuples
# x = ((1,3,4),(5,4,0),(5))
# print(x[0])

# Manipulation des listes
# l1 = [2,4,5,8,10,25, 15]
# l1.append(22)
# print(l1)
# l1.insert(0, 10)
# print(l1)
# # suppresion de l'élément n°3
# del l1[1]
# print("Avant pop")
# print(l1)
# print("exemple après pop")
# l1.pop(1)
# print(l1)

# l1.reverse()
# print(l1)

# l1.extend(l1)
# print(l1)

# # Creation par compréhension
# source = range(1,15)
# resultat = [v*v for v in source]
# print(resultat)

# # Creation par comprehension 2
# resultat2 = [v**2 for v in source if(v%2==0)]
# print(resultat2)

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(start=0, stop=4*np.pi, num = 1000)
# y = [np.cos(a) for a in x]

# plt.plot(x,y)
# plt.show()

# # Manipulation des chaines de caractères

# s1 = "hello world!"
# bjr = list(s1)
# print(bjr)

# decoupe = s1.split("!")
# print(decoupe)


# # Manipulation des dictionnaires
# d = {('c1','c8'):2, 'c2':15, 'c3':71, 'c4':112, 'c5':"papa", 'c6':"strlen"}
# print(len(d))

# print(d.keys())
# print(d.values())

# d["c1"]="Papa"
# print(d)

n = int(input("Nombre d'items :"))
# dictionnaire vide
dico= {}

# saisie
for i in range(0,n):
    cle = "Cle "+str(i)
    valeur = 12*i
    dico[cle] = valeur
    

for (k,v) in dico.items():
    print(k,': ',v)
    
# somme des valeurs
s = 0 
for v in dico.values():
    s = s + v
print(s)