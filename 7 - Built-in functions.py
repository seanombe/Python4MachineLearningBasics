'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

# Les fonctions par défaut

x = -3.14

#abs() pour la valeur absolue

print(abs(x))

#round() pour arrondie

x = round(x)
print(x)

#######################################

# Min, Max Len sur la liste CQFD

List = [1, 3, 5, 6]

print(max(List))
print(min(List))
print(len(List))

# sum() pour sommmer des éléments

print(sum(List))

# all() retourne true si tous les éléments de la liste sont true et any retourne true si au moins 1 est true
# utilisation sur des structures non booléenes 0 est false et le reste true

List1 = [True, False]
print(all(List1))
print(any(List1))


##################################

# Le casting est possible

# input("Texte") retourne une donnée entrée par l'utilisateur mais c'est un string

# format pour le formatage de chaine de caractère

# Open()
with open("file.txt", 'w') as f:
    f.write("1")

