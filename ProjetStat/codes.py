# importation des packages et modules nécéssaires
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
import numpy as np
import scipy
import math

# lecture des données
data = pd.read_csv("insurance.csv", index_col="index")

# apperçu rapide des données
data.head()

# affichage du nombre total d'observations et de variables
n,p = data.shape
print(f"Le jeu de données comporte : {n} individus et {p} variables")

# affichage du nombre de valeurs manquantes par variables
data.isna().sum()

# affichages des types de chaque variables
data.dtypes

# description générales des variables quantitatives
data.describe()

# description générale des variables qualitatives
data.describe(include='object')

# renommage des modalités des variables sex, region et smoker
data["sex"] = data["sex"].replace(["male","female"],["Masculin","Féminin"])
data["smoker"] = data["smoker"].replace(["yes","no"],["Oui","Non"])
data["region"] = data["region"].replace(["southwest","southeast","northwest","northeast"],["Sud-Ouest","Sud-Est","Nord-Ouest","Nord-Est"])

# définition de la fonction qui génère les labels des graphiques
def label_function(val):
    return f'{val/100*len(data):.0f}; {val:.0f}%'

# construction du diagrammes pour la région
data.groupby('region').size().plot(kind="pie", autopct=label_function, 
                                textprops={'fontsize':15})
plt.title("Répartition des individus selon la région de résidence")
plt.ylabel("")

# définition de la fonction qui permet d'ajouter des effecifs sur les
# barres de l'histogramme
def hist_annotate(freq, bins, patches):
    # coordonnées x pour les labels
    bins_centers = np.diff(bins)*0.5+bins[:-1]
    i=0
    # on crée un itérable composé de freq, bins_centers et patches pour
    # le parcours
    for fr, x, patch in zip(freq, bins_centers, patches):
        height = int(freq[i])
        plt.annotate("{}".format(height),
                    xy = (x, height), # coin supérieur gauche de la barre
                    xytext = (0,0.2),
                    textcoords = "offset points",
                    ha = "center", va = "bottom"
                    )

        i = i+1
		
		
# histogrammes pour les variables quantitatives

# cas de l'âge
freq, bins, patches = plt.hist(data["age"], alpha=1, edgecolor='black')
hist_annotate(freq = freq, bins = bins, patches = patches)
plt.xlabel("Ages (en années)")
plt.ylabel("Effectifs")
plt.title("Histogramme des ages")
plt.show()


# cas de l'IMC
freq, bins, patches = plt.hist(data["bmi"], bins=20,alpha=1, edgecolor="black")
hist_annotate(freq = freq, bins = bins, patches=patches)
plt.xlabel("IMC (en Kg/m^2)")
plt.ylabel("Effectifs")
plt.title("Histogramme de l'IMC")
plt.show()

# cas du nombre d'enfants
freq, bins, patches = plt.hist(data["children"], edgecolor="black")
hist_annotate(freq, bins, patches)
plt.xlabel("Nombre d'enfants")
plt.ylabel("Effectifs")
plt.title("Histogramme du nombre d'enfants")
plt.show()


# cas des charges
freq, bins, patches = plt.hist(data["charges"], bins=15, edgecolor="black")
hist_annotate(freq, bins, patches)
plt.xlabel("Frais d'assurance (en $)")
plt.ylabel("Effectifs")
plt.title("Histogramme des frais d'assurance")
plt.show()

# Création de la colonne des logarithmes des charges
data["logCharges"] = np.log(data["charges"])
# Appercu des 5 premières lignes des logCharges
data["logCharges"].head()

# histogramme des logCharges
freq, bins, patches = plt.hist(data["logCharges"], bins=15, edgecolor="black")
hist_annotate(freq, bins, patches)
plt.xlabel("Logarithmes de Frais d'assurance (en $)")
plt.ylabel("Effectifs")
plt.title("Histogramme des logarithmes des frais d'assurance ")
plt.show()

# matrice des corrélations pour les variables quantitatives
sns.set(rc = {'figure.figsize':(10,4)})
data_corr = data.corr()
ax = sns.heatmap(data_corr, xticklabels=data_corr.columns,
                yticklabels=data_corr.columns, cmap='coolwarm')

# diagrammes de boites à moustaches des charges selon le sexe
sns.catplot(x='sex', y = 'charges', data = data, kind = 'box')
plt.xlabel("Sexe")
plt.ylabel("Frais d'assurances en $")
plt.title("Boxplot frais d'assurance vs. sexe")

# diagrammes de boites à moustaches des charges selon smokder
sns.catplot(x='smoker', y = 'charges', data = data, kind = 'box')
plt.xlabel("Consommation de tabac")
plt.ylabel("Frais d'assurances en $")
plt.title("Boxplot frais d'assurance vs. Fumer")

# diagrammes de boites à moustaches des charges selon la région
sns.catplot(x='region', y = 'charges', data = data, kind = 'box')
plt.xlabel("Régions")
plt.ylabel("Frais d'assurances en $")
plt.title("Boxplot frais d'assurance vs. Région")


# diagrammes de boites à moustaches des charges selon le nombre d'enfants
sns.catplot(x='children', y = 'charges', data = data, kind = 'box')
plt.xlabel("Nombre d'enfants")
plt.ylabel("Frais d'assurances en $")
plt.title("Boxplot frais d'assurance vs. Région")


# test de normalité pour l'âge
pg.normality(data['age'])

# test de normalité pour l'IMC
pg.normality(data['bmi'])

# test de normalité pour le frais d'assurances
pg.normality(data['charges'])

# test de normalité pour le nombre d'enfants
pg.normality(data['children'])

# nuage de points entre les charges et l'âge
sns.scatterplot(x= 'age', y = 'charges', data = data, hue = 'smoker')
plt.xlabel("Age (en années)")
plt.ylabel("Charges d'assurance (en $)")
plt.title("Age Vs. Charges d'assurances")


# nuage de points entre les charges et l'IMC
sns.scatterplot(x= 'bmi', y = 'charges', data = data, hue = 'smoker')
plt.xlabel("IMC (kg/m^2)")
plt.ylabel("Charges d'assurance (en $)")
plt.title("IMC Vs. Charges d'assurances")


# test de student entre le sexe et les charges
pg.ttest(x = data[data['sex']=='male']['charges'],y = data[data['sex']=='female']['charges'])

# test de student entre le smoker et les charges
pg.ttest(x = data[data['smoker']=='yes']['charges'],y = data[data['smoker']=='no']['charges'])

# entre la région et les charges
scipy.stats.f_oneway(
    data[data['region']=='Sud-Ouest']['charges'], 
    data[data['region']=='Sud-Est']['charges'],
    data[data['region']=='Nord-Ouest']['charges'],
    data[data['region']=='Nord-Est']['charges'])
# on peut affirmer avec un faible risque de se tromper qu'au moins deux moyennes 
# diffèrent. Autrement dit il y'a une influence significative de la région sur les 
# dépenses d'assurances


# entre le nombre d'enfants et les charges
scipy.stats.f_oneway(
	data[data['children']==0]['charges'],
	data[data['children']==1]['charges'], 
	data[data['children']==2]['charges'],
	data[data['children']==3]['charges'],
	data[data['children']==4]['charges'],
	data[data['children']==5]['charges'])
# on peut affirmer avec un faible risque de se tromper qu'au moins deux moyennes diffèrent. Autrement dit 
# il y'a une influence significative du nombre d'enfants sur les dépenses d'assurances























