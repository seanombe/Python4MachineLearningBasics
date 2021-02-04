'''
@Auteur : Sean OMBE
@Mail : patrick.ombe@gmail.com
'''

import numpy as np
import matplotlib.pyplot as plt


def printfigure(dataset = {}):
    plt.figure(figsize=(16, 9))

    ngraph = len(dataset)

    for k, v in enumerate(dataset.values()):
        plt.subplot(ngraph, 1, k+1)
        x = np.linspace(0, 50,len(v))
        plt.plot(x, v, label="Ligne")
        plt.legend()
        plt.title("Fig {}".format(k+1))
        pass

    #gerer le les marges
    plt.tight_layout(pad=0.3, w_pad=2.0, h_pad=5.0)
    plt.show()

data = { f"experience{i}" : np.random.randn(100) for i in range(4)}
printfigure(data)

