'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

#Ceci est la fonction de fibonacci
def fibonacci(n = 0):
    if (n == 0):
        return 1
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)