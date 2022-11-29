# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:57:52 2022

@author: OWONA Edouard
"""

# Le but de ce module est d'implémenter les fonctions ci-après:
# 1. Equation degré 1
# 2. Equation degré 2
# 3. Parité 
from math import sqrt

def equationDeg1(b,c):
    if(b==0):
        if(c==0):
            print("Infinite de solutions")
        else:
            print("L'equation est insuluble ")
    else:
        print("La solution est: ",-c/b)
    
def prixTTC(prix):
    # #  Demande du prix hors-taxe
    # cast et calcul du prix TTC
    pht = float(prix)
    pttc = pht*1.20
    # affichage du prix TTC
    print("prix TTC: "+ str(pttc))    
    
def tableMultiplication(a):
    for i in range(1,12):
        print(str(i)+" x "+ str(a) + " = "+str(a*i))


def tableMultiplication2(a):
    i = 1
    while (i<12):
        print(str(i)+" x "+ str(a) + " = "+str(a*i))
        i+=1
        
        
        
# fonction pour résoudre une équation du second degré
def equations(a,b,c):
# =============================================================================
#   The target of this function is to solve a quadratic equation
#   We get the a, b and c coefficients and verify the diffrent cases
#   if a=b=c=0 then we the an infinity of solutions 
# =============================================================================
   
    if(a == 0):
        equationDeg1(b, c)        
    else:
        delta = float(b*b-4*a*c)
        if(delta<0):
            print("L'équation n'admet pas de racines !!!")
        elif(delta==0):
            print("L'unique solution est : ", -b/(2*a))
        else:
            print("Les solutions sont : x_1 ="+ str(((-b-sqrt(delta))/(2*a))) + " x_2 = "+ str(((-b+sqrt(delta))/(2*a))))    

def parite(a):
    if(a%2 == 0):
        print("La nombre est pair ")
    else:
        print("Le nombre est impair ")



    
    