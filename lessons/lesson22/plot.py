import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.legend()
plt.show()