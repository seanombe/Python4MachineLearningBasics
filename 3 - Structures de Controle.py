'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

def classification_age(n):
    # If/Elif/Else
    if (n <= 18):
        return "Mineur"
    elif ( n > 18) and ( n <= 60):
        return "Dans la fleur de l'âge"
    else :
        return "Retraité"

def entree_age():
    age = input("Entrez l'âge (>=0)\n")
    # While
    while (int(age) <= 0):
        age = input("Entrez l'âge (>=0)\n")
    return age

def main():
    age = int(entree_age())
    # For
    for i in range(age):
        print(classification_age(age))

    print("\n")

    for i in range(1,5,1):
        print(classification_age(age))

#Lancement
main()