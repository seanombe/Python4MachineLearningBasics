# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:59:14 2021

@author: patri
"""

import numpy as np

np.random.seed(0)


def standardisation_matrice_par_colone(mat):
    mat = mat.dot(1.0)

    nb_ligne = mat.shape[0]
    nb_colonne = mat.shape[1]

    liste_moyenne = mat.sum(axis=0) / nb_ligne
    liste_variance = np.std(mat, axis=0)

    mat = mat.dot(1.0)

    for i in range(nb_colonne):
        mat[:, i] = (mat[:, i] - liste_moyenne[i]) / liste_variance[i]

    return mat


A = np.random.randint(0, 100, [10, 5])

b = standardisation_matrice_par_colone(A)

print(b)



