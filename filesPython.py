# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:44:00 2022

@author: By237Fact
"""

import csv
import classes as MP
import json
import xml.etree.ElementTree as ET

# p = open("fichier.txt","r", encoding="utf-8")
# # print(p.read())
# ls = p.readlines()
# print(ls)
# p.close()

# f = open("personnes.csv","r",encoding="utf-8")
# lecteur = csv.reader(f, delimiter=";")
# for ligne in lecteur:
#      # dans le cas des listes, on accèdes aux champs à l'aide des indices
#     print(ligne[0])

# f.close()



# f = open("personnes.csv","r",encoding="utf-8")
# lecteur = csv.DictReader(f, delimiter=";")
# for ligne in lecteur:
#       # dans le cas des dictionnaires, on accèdes aux champs à l'aide des
#       # noms des champs
#     print(ligne["age"])

# f.close()


# p = MP.Personne()
# p.saisie()
# f = open("personne.json","w")

# d = {"Nom": p.nom,"Age": p.age,"Salaire":p.salaire}
# json.dump(d,f)
# f.close()

""" 
    Codes pour le json
"""
# Sauvegarder un ensemble de personnes
# n = 50
# f = open("personne.json","a")
# listePers = []
# for i in range(0,n):
#     a = MP.Personne()
#     a.setValues("Nom "+ str(i+1),10*(i+1),"Prenom "+ str(i+1))
#     listePers.append(a)

# f = open("personnes.json","w")
# tmp = []
# for p in listePers:
#     d = {}
#     d["Nom"] = p.nom
#     d["Age"] = p.age
#     d["Salaire"] = p.salaire
#     tmp.append(d)
# json.dump(tmp, f)
# f.close()

# # charger un ensemble de personnes
# f = open("personnes.json","r")
# tmp = json.load(f)
# liste = []
# for d in tmp:
#     # creer une personne
#     p = MP.Personne()
#     p.nom = d["Nom"]
#     p.age = d["Age"]
#     p.salaire = d["Salaire"]
#     p.affichage()
#     liste.append(p)
# print("\nNb personnes :", len(liste))
# f.close()

""" 
    Codes pour le xml
"""

# # Saisie des informations de personne
# p = MP.Personne()
# p.setValues("Personne 1",25,1542.52)

# # ecriture racine
# root = ET.Element("Personne")

# # Ecriture des éléments
# item_nom = ET.SubElement(root, "Nom")
# item_nom.text = p.nom

# item_age = ET.SubElement(root, "Age")
# item_age.text = str(p.age)

# item_salaire = ET.SubElement(root, "Salaire")
# item_salaire.text = str(p.salaire)

# # Sauvegarder dans un xml
# tree = ET.ElementTree(root)
# tree.write("personne.xml")


# # ouverture
# tree = ET.parse("personne.xml")

# # récupérer les racines
# root = tree.getroot()

# # transformation en Personne
# p = MP.Personne()
# p.nom = root.findtext("Nom")
# p.age = int(root.findtext("Age"))
# p.salaire = float(root.findtext("Salaire")) 

# p.affichage()


"""
    xml avec la variante des balises
"""

# Saisie des informations de personne
p = MP.Personne()
p.setValues("OWONA",48,152.52)

# ecriture racine
root = ET.Element("Personne")

# associer un attribut à la balise Personne
root.set("Nom", p.nom)

root.set("Age", str(p.age))
root.set("Salaire", str(p.salaire))

tree = ET.ElementTree(root)
tree.write("personne.xml")

p = MP.Personne()
p.nom = root.get('Nom')
p.age = int(root.get('Age'))
p.salaire = float(root.get('Salaire'))

p.affichage()



