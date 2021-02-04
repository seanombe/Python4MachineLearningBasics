'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

import numpy as np
# AXIS = 0 LIGNE
# AXIS = 1 COLONNE
# AXIS = 2 PROFONDEUR

np.random.seed(1)

tab = np.random.randn(6,6)
print(tab)

# Indexing c'est toucher le tableau via les index

print(tab[1,3])

# Slicing c'est pousser des rangés via les index
tab[1:-1,1:-1] = 0
print(tab)
# -1 est mis pour l'avant dernier élément


tab = np.random.randint(1, 10, [5,6])
print(tab)

# Masking c'est toucher un tableau avec des conditions

tab[tab>4] = 0
print(tab)