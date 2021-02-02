'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

# Tuples
'''
Les tuples sont des entites non modifiables,
peuvent contenir tout type 
de variables sauf les dictionnaires
'''
tuple_1 = (1, 2, 4)
print(tuple_1)

# Listes
'''
Les listes peuvent contenir tout type 
de variables sauf les dictionnaires
'''

# Créer une liste
liste_1 = [1,3,4,6,7,10]
villes = ['Paris','Berlin','Londres','Bruxelles']

# Ajouter des listes à une liste
nested_liste = [liste_1,villes]
print(nested_liste)

# Ajout dans une liste
nested_liste.append("Sean")
print(nested_liste)

# Rajoute un élément a l'index indiqué
villes.insert(2, 'Madrid')
print(villes)

# Rajoute une liste a la fin de notre liste
villes.extend(['Amsterdam', 'Paris'])
print(villes)

# Affiche la longueur de la liste
print('longeur de la liste:', len(villes))

# Trie la liste par ordre alphabétique / numérique
villes.sort(reverse=False)
print(villes)

# Compte le nombre de fois qu'un élément apparait dans la liste
print(villes.count('Paris'))

# Supprimer un élément pop(i)
print(villes.pop())

if 'Paris' in villes :
    print("Oui")
else :
    print("Non")

# Parcours d'une liste
for city in villes :
    print(city)

# Parcours de deux listes en parallèle (dont une des plus courte, cela se stoppe où la plus courte se stoppe)
for city, city1 in zip(villes, nested_liste) :
    print(city1, city)
