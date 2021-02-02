'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

#Ici on apprendra à déclarer des variables

#Déclarer une variable
x = 1
prompt = "Ceci est une chaîne de caractère"

#On peut créer plusieurs variables
z, y = 2, 'Sean'

#Afficher une variable
print(x)
print(prompt)
print(z, y)

#Ici on apprendra à déclarer des fonctions

#Ceci est la fonction de fibonacci
def fibonacci(n = 0):
    if (n == 0):
        return 1
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

#Ceci est la fonction principale
def main():
    print(fibonacci(5))

#Lancement
main()