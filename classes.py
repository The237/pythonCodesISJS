 # -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:37:46 2022

@author: By237Fact
"""


class Personne:
    """ Classe Personne """
    
    # variable de classe
    compteur = 0 
    
    def __init__(self):
        # Lister les propriétés
        self.nom = " "
        self.age = 0
        self.salaire = 0.0
        Personne.compteur+=1
        # fin du constructeur
    
    def saisie(self):
        self.nom = input("Nom : ")
        self.age = int(input("Age : "))
        self.salaire = float(input("Salaire : "))
        # fin saisie
    def setValues(self,nom, age, salaire):
        self.nom = nom
        self.age = age
        self.salaire = salaire
    
    def affichage(self):
        print("\nSon nom est : ", self.nom)
        print("Son age est : ", self.age)
        print("Son salaire est : ", self.salaire)
        # fin affichage
    
    def retraite(self, limite):
        reste = limite - self.age
        if(reste<0):
            print("Vous etes à la retraite")
        else:
            print("Il vous reste %s annees"% (reste))
        # fin retraite

# Plus loin avec les classes
# Abstraction : capacité à visualiser les choses dans leur globalité
class Employe(Personne):
    def __init__(self):
        Personne.__init__(self)
        self.prime = 0.0
    # fin constructeur
    
    def saisie(self):
        Personne.saisie(self)
        self.prime = float(input("Prime : "))
    # fin saisie
    
    def affichage(self):
        Personne.affichage(self)
        print("Sa prime est : ", self.prime)

    def setValues(self, nom, age, salaire,prime):
        Personne.setValues(self, nom, age, salaire)        
        self.prime = prime
        
# fin de la classe employé