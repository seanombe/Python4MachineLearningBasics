'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''
import time

# List Dict comprehension
# 1 CE QUI VEUT FAIRE
# 2 NOTRE BOUCLE FOR
# 3 LES CONDITIONS SUR LES ELEMENTS


liste1 = []

start = time.time()

for i in range(20000):
    liste1.append(i**2)

end = time.time()
print("Le temps mis normal est {}".format(end-start))

## AVEC LES LIST COMPREHENSIONS, on a un code plus réduit et plus rapide
start = time.time()

liste1 = [(i**3) for i in range(20000)]

end = time.time()
print("Le temps mis via listcomp est {}".format(end-start))

#CA PEUT FAIRE LA DIFFERENCE A HAUT NIVEAU LA DIFFERENCE DE DELAY

#Une nasty list est une liste qui contient d'autres liste

#Cela est valable pour les dictionnaires
dico = {
    0 : "Pierre",
    1 : "Jean",
    2 : "Paul",
    3 : "Iris"
}
print(dico.items())

#On va recrée le dictionnaire au dessus avec moins de ligne
liste_prenom = ["Pierre","Jean","Paul","Iris"]
dico = { k:v for k, v in enumerate(liste_prenom)}
print(dico.items())

liste_age = [12,14,15,50]
dico = { prenom:age
         for prenom, age in zip(liste_prenom, liste_age)
         if age > 20 }
print(dico.items())

# On veut bien l'utiliser pour les tuples mais on devra faire du transtipage
# Cela va creer un object qui n'est pas un tuple
tuple_1 = (i**2 for i in range(5))
print(type(tuple_1))

# Nous allons donc faire du cast !
tuple_1 = tuple((i**2 for i in range(5)))
print(tuple_1)

