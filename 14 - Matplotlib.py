'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2, 50)


#1 Créer d'abord la figure
plt.figure(figsize=(12,8)) # on est en inches

# il doit y avoir le meme nombre d'éléments dans les deux tableaux

# plot c'est pour les lignes
plt.plot(x,x**2, label="Ligne")

# les attributs de plot
# label pour le nom de la courbe
# lw pour epaisseur
# ls pour le style de trait
# c  pour la couleur du trait

# scatter c'est pour les lignes en petit point
plt.scatter(x, x**3, color="red", label="Point")


plt.xlabel("Abscisse")
plt.ylabel("Ordonnée")
plt.legend()
plt.title("La figure 1")
#plt.savefig('figure.png')
plt.show()

#########################
# ------> TITRE : plt.title("titre")
# ------> Nom des axes x : plt.xlabel("")
# ------> Nom des axes y : plt.ylabel("")
# ------> Legende : plt.legend() ne pas oublier de mettre les label
# ------> Sauver une figure : plt.savefig('figure.png')
# ------> Montrer le graphique : plt.show()

##########################################

# Plusieurs graph sur une seule figure

plt.figure(figsize=(12,8))

plt.subplot(1,2,1)
plt.plot(x,x**2, label="Ligne")
plt.xlabel("Abscisse")
plt.ylabel("Ordonnée")
plt.legend()
plt.title("La fonction x puissance 2")



plt.subplot(1,2,2)
plt.scatter(x, x**3, color="red", label="Point")
plt.xlabel("Abscisse")
plt.ylabel("Ordonnée")
plt.legend()
plt.title("La fonction x puissance 3")


plt.savefig('figure.png')

#ca finit par show
plt.show()