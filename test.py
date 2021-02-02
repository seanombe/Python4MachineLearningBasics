import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x = np.linspace(0, 2, 10)
y = x**2
plt.plot(x, x**3, label = 'Puissance 3')
plt.plot(x, x**4, label = 'Puissance 4')
plt.title('figure 1')
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.legend()
plt.show()
plt.savefig('figure.png')