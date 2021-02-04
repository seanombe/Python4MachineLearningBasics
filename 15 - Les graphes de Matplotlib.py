'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''


import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D

# charger le dataset
iris = load_iris()
x = iris.data
y = iris.target
names = list(iris.target_names)

print(f'x contient {x.shape[0]} exemples et {x.shape[1]} variables')
print(f'il y a {np.unique(y).size} classes')
#print(x)
#print(y)


##############################################
################   GRAPHE DE NUAGE DE POINT
# plt.scatter()
### En général c'est pour voir la correlation entre des variables

# On va analyser les deux premières variables
plt.figure(figsize=(12,9))
plt.subplot(2,2,1)
plt.xlabel("Longueur du sépal")
plt.ylabel("Largeur du sépal")
plt.scatter(x[:,0], x[:,1])
#plt.show()
###C'est bien mais bof

### On va faire du coloriage selon la nature de leur classe
plt.subplot(2,2,2)
plt.scatter(x[:,0], x[:,1], c = y)
plt.xlabel("Longueur du sépal")
plt.ylabel("Largeur du sépal")

#### On peut gerer la transparence de nos éléments (apha) et la taille (s)
plt.subplot(2,2,3)
plt.scatter(x[:,0], x[:,1], c=y, alpha=0.5, s=100)
plt.xlabel("Longueur du sépal")
plt.ylabel("Largeur du sépal")

### On peut gérer la taille en fonction d'une variable également
plt.subplot(2,2,4)
plt.scatter(x[:,0], x[:,1], c=y, alpha=0.5, s=x[:,2] * 100)
plt.xlabel("Longueur du sépal")
plt.ylabel("Largeur du sépal")
plt.colorbar()

#plt.show()



##############################################
################   GRAPHE 3D
plt.figure(figsize=(12,9))

ax = plt.axes(projection='3d')
ax.scatter(x[:,0], x[:,1],x[:,2], c=y, alpha=0.5, s=x[:,3] * 100)
ax.set_title("Vue tri-dimensionnelle 😊")
ax.set_xlabel("1er dimension")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2eme dimension")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3eme dimension")
ax.w_zaxis.set_ticklabels([])

#plt.show()

f = lambda x,y : np.sin(x) + np.cos(x+y)
#### essaie sur une fonction
plt.figure(figsize=(12,9))
X = np.linspace(0,5, 100)
y = np.linspace(0,5, 100)
X, y = np.meshgrid(X,y)
z = f(X,y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, y, z, cmap = "plasma")
ax.set_title("Vue tri-dimensionnelle 😊")
ax.set_xlabel("1er dimension")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2eme dimension")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3eme dimension")
ax.w_zaxis.set_ticklabels([])

#plt.show()


##############################################
################   HISTOGRAMME

# on peut voir les valeurs prises par des variables
# leur distribution
plt.figure(figsize=(12,9))
plt.subplot(2,2,1)
plt.hist(x[:,0])

###On peut vouloir modifier le nombre de section qu'on a dans notre graphe
# On utilise le paramètre bins
plt.subplot(2,2,2)
plt.hist(x[:,0], bins=20)

#on peut afficher plusieurs histogrammes
plt.subplot(2,2,3)
plt.hist(x[:,0], bins=20)
plt.hist(x[:,1], bins=20)

#### on peut décider de tracer un histogrammme en 2d
plt.subplot(2,2,4)
plt.hist2d(x[:,0], x[:,1], cmap = "Blues")
plt.xlabel('Longueur')
plt.ylabel('Largeur')
plt.colorbar()

#plt.show()


##############################################
################   CONTOUR PLOT
### les parties en traits plein sont les points qu'on vise

plt.figure(figsize=(12,9))
plt.subplot(3,1,1)
plt.contour(X,y,z)


plt.subplot(3,1,2)
plt.contour(X,y,z, 20, colors='black')

plt.subplot(3,1,3)
plt.contourf(X,y,z, 20, cmap='RdGy')
plt.colorbar()

#plt.show()


##############################################
################   imshow

plt.figure(figsize=(12,9))
plt.imshow(np.corrcoef(x.T), cmap="RdGy")
plt.colorbar()


plt.show()