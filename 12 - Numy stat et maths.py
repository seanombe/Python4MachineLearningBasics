'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

import numpy as np

np.random.seed(1)

A = np.random.randint(0, 10, [4,3])
print(A)

# Somme selon les axes / nous retourne une liste
# Min / Max possible aussi
# Trouver la position du minimum et du maximum avec argmin/argmax
# On obtient des listes
print(A.sum(axis=1))

# Argsort
# retourne la fonction avec laquelle on doit placer les indexes pour
# obtenir un certain ordre

print(A.argsort(0))


# Moyenne c'est mean(axis)
# Ecart type c'est std(axis)
# Variance c'est var(axis)


# Corrcoef(A) le lien entre des éléments
# Plus c'est proche des extrèmes mieux ca vaut
# cela signifie dans le cas positif que l'évolution d'une variable 
# entraine la chute de l'autre
# le contraire dans le cs negatif
print(np.corrcoef(A))

# On peut avoir aussi le nombre d'occurence de certains éléments
#print(np.unique(A,return_counts=True))

# Utilisons argsort

values, occur = np.unique(A, return_counts=True)
print(values, occur)

# cherchons les index pour trier occur
print(occur.argsort())

# on injecte ca dans values et on aura un tableau classé
print(values[occur.argsort()])

# Gerer les nan ( not a number)
A = np.random.randn(5,5)

A[2,1] = np.nan
A[2,2] = np.nan

#calculer la moyenne, variance ... peut se faire sans les gérer
# cela va ignorer les nan

print(np.nanmean(A))

# voir les nan via booleens

print((np.isnan(A).sum()/A.size))

#se débarasser des nan

A[np.isnan(A)] = 0
print(A)

# LE PRODUIT DE MATRICE A.dot()