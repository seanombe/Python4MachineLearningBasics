'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

#Le dictionnaire est une structure de données non ordonnée
#Ensemble d'association clé valeur c'est pas ordonné


dico = {
    "cle1" : 'sean',
    "cle2" : 'kevin'
}

#la taille du dico
print(len(dico))

#Ajouter une élément
dico["cle3"] = ['sean', 'kevin']

#Modifier la valeur d'un champ
dico["cle1"] = 'Patrick'

#Pour sortir  les clés
print(dico.keys())

#Pour sortir les valeurs
print(dico.values())

#Pour sortir clé et valueur
print(dico.items())

#Chercher une valeur dans le dico via sa clé (none si il y a rien)
print(dico.get("cle4", 'Il y a pas ça'))

#Creer un dico avec les clés et donner une valeur par défaut
listedekeys = ["dakar", "thies", "new-york"]

#Retier une association du dico
print(dico.pop("cle3"))

#For
for i, v in dico.items():
    print(i,v)