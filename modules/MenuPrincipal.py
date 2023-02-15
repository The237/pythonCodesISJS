# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:59:53 2022

@author: OWONA Edouard
"""

import equationsParite

def menuPrincipal():
    q = False
    print('***************************************\n************ Menu Principal************\n***************************************\n')
    while(q!=True):     
        print("\n\n1. Calcul du prix TTC\n2. Résolution d'une equation simple\n3. Résolution d'une equation quadratique\n4. Table de multiplication\n5. Multiplication v2\n6. Parite nombre \n7. Quitter")
        choix = int(input("\nVeuillez faire un choix : "))
        if(choix ==1):
            pht = input("prix HT: ")
            equationsParite.prixTTC(pht)
        elif(choix==2):
            a = float(input("Entrez le coef. a: "))
            b = float(input("Entrez le coef. b: "))
            equationsParite.equationDeg1(a, b)

        elif(choix==3):
            # Lecture des arguments
            a = float(input("Entrez le coef. a: "))
            b = float(input("Entrez le coef. b: "))
            c = float(input("Entrez le coef. c: "))
            equationsParite.equations(a, b, c)
        elif(choix==4):
            a = int(input("Nombre à multiplier: "))
            equationsParite.tableMultiplication(a)
        elif(choix==5):
            a = int(input("Nombre à multiplier: "))
            equationsParite.tableMultiplication2(a)
        elif(choix==6):
            a = int(input("Entrez un nombre : "))
            equationsParite.parite(a)
        elif(choix==7):
            q = True
        else:
            print("!!! Choix invalide !!!\n")


menuPrincipal()