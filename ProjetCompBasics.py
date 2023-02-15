# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:58:05 2023

@author: OWONA Edouard
"""

import pandas as pd
import numpy as np


# 1. Code de la première fonctionnalité
#  Fonction de lecture des données et retour du data frame
def lireDonnees(path, sep ,names):
    
    array = np.loadtxt(path)

    df = pd.DataFrame(data = array, columns=names)
    # cast des villes en int afin de favoriser le remplacement pas les noms de villes
    df["NomRegion"] = df["NomRegion"].astype(int)
    df["NomRegionVoisine"] = df["NomRegionVoisine"].astype(int)
    
    return df


#  Fonction de création des numéros de villes
def creerNumsVilles(n=20):
    numVilles = []
    numVilles.append(-1)
    for x in range(20):
        numVilles.append(x)
    return numVilles

#  Fonction de remplacement des numéros de villes
def remplacerNumVilles(data, numVilles, listeVilles):
    data["NomRegion"] = data["NomRegion"].replace(numVilles, listeVilles)
    data["NomRegionVoisine"] = data["NomRegionVoisine"].replace(numVilles, listeVilles)
    return data



def plusGrandeLongFront(data):
    return data['LongFrontiere'].max()

def plusGrandeDistCentroide(data):
    return data['DistCentroide'].max()

def regionsGrandeFront(data):
    indexMaxFront = data["LongFrontiere"].idxmax()
    print('Les région concernées sont (frontieres) :\n')
    print("La region est :", data["NomRegion"][indexMaxFront],"\n")
    print("Sa voisine est :",data["NomRegionVoisine"][indexMaxFront],"\n")

def centroidesRegionsGrandeFront(data):
    indexMaxCent = data["DistCentroide"].idxmax()
    print('Les région concernées sont (centroides) :\n')
    print("La region est :", data["NomRegion"][indexMaxCent],"\n")
    print("Sa voisine est :",data["NomRegionVoisine"][indexMaxCent],"\n") 
    

    
""" 

    Test de la première fonctionnalité

"""
# définition des noms de colonnes
colonnes=["NomRegion","NomRegionVoisine","DistCentroide","LongFrontiere"]

# # définition des noms des villes
villes = ["pas de voisin","abruzzo", "apulia", "basilicata",  "calabria", "campagna", "emiliaromagna", 
            "friuli", "lazio", "liguria", "lombardia", "marche", "molise" ,"piemonte", 
              "sardegna", "sicily", "toscana", "trentino", "umbria" , "valledaosta" , "veneto"]

numVilles = creerNumsVilles(20)


data = lireDonnees("data/donnesCartes.txt","\t", names=colonnes)

dataTreated = remplacerNumVilles(data, numVilles = numVilles, listeVilles=villes)


# Creation du csv et du xlsx correspondant


dataTreated.to_csv("data/donneesTraitee.csv")
dataTreated.to_excel("data/donneesTraitee.xlsx")

print("----------------- Test de la fonctionnalité 1 --------------------\n")
print('Les fichiers ont bien été crés dans le répertoire courant data\n')

""" 

    Test de la seconde fonctionnalité

"""

print("\n----------------- Test de la fonctionnalité 2 --------------------\n")

print("La plus grande longueur de frontière est : ",plusGrandeLongFront(data), "\n")
regionsGrandeFront(data)


""" 

    Test de la troisième fonctionnalité

"""

print("\n----------------- Test de la fonctionnalité 3 --------------------\n")

print("La plus grande longueur de centroide est : ",plusGrandeDistCentroide(data), "\n")
centroidesRegionsGrandeFront(data)


print("\n----------------- Test de la fonctionnalité 4 --------------------\n")
print("La distance moyenne entre les centroïde est : ",round(data["DistCentroide"].mean(),2), "\n")


print("\n----------------- Test de la fonctionnalité 5 --------------------\n")
print("La longueur moyenne des frontières est : ",round(data["LongFrontiere"].mean(),2), "\n")
