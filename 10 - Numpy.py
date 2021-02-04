'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

import numpy as np
import matplotlib.pyplot as plt
#On va travailler avec les ndarray qui peuvent avoir de 1 à 3 dimensions

# Souvent en machine learning on travaillera avec les tableaux 2 dimensions

# Ce sont des objets et ils ont des attributs et fonctions

# Plusieurs constructeurs possibles

# ARRAY()

tab = np.array([1,2,3])

    # L'attribut shape permet de donner les dimensions, shape donne des TUPLES
    # On peut donc utiliser shape pour avoir le nombre lignes et colones
    # On peut avoir aussi sa dimension ndim
    # Size pour avoir le nombre d'éléments du tableau

print(tab.size)
print(tab.shape)


# ZEROS et ONES (shape du tableau sous forme de tuple)

tabz = np.ones((3,6))
print(tabz)

tabo = np.zeros((3,6))
print(tabo)

# full c'est pour initialiser avec un nombre
tabf = np.full((4,7), 5)
print(tabf)

np.random.seed(0)
# Creer un tableau avec des valeurs aléatoires de la distributions nombre centrée en 0, on met
# pas de tuples ici juste les dimensions
tabn = np.random.randn(4,3)
print(tabn)


# LINSPACE : Créer un tableau à une dimension (debut, fin, nombre élément)
ligne = np.linspace(1, 20, 40)

plt.figure()
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.plot(ligne, ligne)
#plt.show()
# ET ARRANGE : Créer un tableau à une dimension (debut, fin, pas)

## DTYPE pour définir le type de nos valeurs pour le type d'éléments


# méthode pour jouer avec les tableaux
# fusionner des tableaux selon un axe avec
# Concatenate ((tab1, tab2, axis=0)) ca depend de l'axe


## Remanier la forme d'un tableau ca marche uniquement si les deux font le meme nombre d'éléments
# avec reshape en donnant un typle
tabn = np.reshape(tabn,(6,2))
print(tabn)

# la tableau tab de départ pose un problème, il est de shape (3,) c'est incomplet
# et c'est possiblement une source de future erreur
# on va donc mettre un 1
tab = tab.reshape((tab.shape[0], 1))
print(tab.shape)

# Si on veut creer des graphiques ou affachier une image à l'écran parfois vaut mieux
# ne pas avoir le 1 en question si on veut faire un retour à (3,)
# on utilise squezze
tab = tab.squeeze()
print(tab.shape)

### RAVEL permet d'applatir un tableau sur un dimension
tabn = tabn.ravel()
print(tabn)