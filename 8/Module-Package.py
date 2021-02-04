'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

from fibo import *
from random import *
import os
import glob
import statistics as stat
import math
import matplotlib # Matplotlib est un package

# Pour fixer notre expérience
seed(1)

liste = [ (fibonacci(i)) for i in range(10) ]

# Il y a beaucoup de fonctions voir la doc

#Moyenne
print(stat.mean(liste))

#Variance
print(stat.variance(liste))


# RANDOMMMMM !!!!

# Choix dans une liste
print(sample(range(100), 10))
print(choice(liste))

# Mélanger des éléments
shuffle(liste)

#randint(start, end), random pour générer des nombre int et float


#############

# Connaitre son répertoire de travail
print(os.getcwd())

###############

#Glob retourne les noms de tous les fichiers de notre répertoire

listefile = glob.glob("*.py")

#afficher sur la console le contenu de nos documents .py

for fichier in listefile:
    with open("{}".format(fichier), 'r') as f:
        print(f.read())



#f.read.splitlines() # recuperer les lignes d'un document sans avoir les \n