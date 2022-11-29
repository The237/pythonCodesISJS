from math import sqrt


def prixTTC(prix):
    # #  Demande du prix hors-taxe
    # cast et calcul du prix TTC
    pht = float(prix)
    pttc = pht*1.20
    # affichage du prix TTC
    print("prix TTC: "+ str(pttc))


# fonction pour résoudre une équation du second degré
def equations(a,b,c):
# =============================================================================
#   The target of this function is to solve a quadratic equation
#   We get the a, b and c coefficients and verify the diffrent cases
#   if a=b=c=0 then we the an infinity of solutions 
#    
#
# =============================================================================
    if(a == 0):
        if(b==0):
            if(c==0):
                print("Infinite de solutions")
            else:
                print("L'équation est insoluble !")
        else:
            print("La solution est :", -c/b)        
    else:
        delta = float(b*b-4*a*c)
        if(delta<0):
            print("L'équation n'admet pas de racines !!!")
        elif(delta==0):
            print("L'unique solution est : ", -b/(2*a))
        else:
            print("Les solutions sont : x_1 ="+ str(((-b-sqrt(delta))/(2*a))) + " x_2 = "+ str(((-b+sqrt(delta))/(2*a))))    


# =============================================================================
# Define a function that give the table of multiplication from 1 to a given
# number
# =============================================================================
def tableMultiplication(a):
    for i in range(1,12):
        print(str(i)+" x "+ str(a) + " = "+str(a*i))


def tableMultiplication2(a):
    i = 1
    while (i<12):
        print(str(i)+" x "+ str(a) + " = "+str(a*i))
        i+=1

def menuPrincipal():
    q = False
    print('***************************************\n************ Menu Principal************\n***************************************\n')
    while(q!=True):     
        print("\n\n1. Calcul du prix TTC\n2. Résolution d'une equation quadratique\n3. Table de multiplication\n4. Multiplication v2\n5. Quitter")
        choix = int(input("\nVeuillez faire un choix : "))
        if(choix ==1):
            pht = input("prix HT: ")
            prixTTC(pht)
        elif(choix==2):
            # Lecture des arguments
            a = float(input("Entrez le coef. a: "))
            b = float(input("Entrez le coef. b: "))
            c = float(input("Entrez le coef. c: "))
            equations(a, b, c)
        elif(choix==3):
            a = int(input("Nombre à multiplier: "))
            tableMultiplication(a)
        elif(choix==4):
            a = int(input("Nombre à multiplier: "))
            tableMultiplication2(a)
        elif(choix==5):
            q = True
        else:
            print("!!! Choix invalide !!!\n")
            
menuPrincipal()