import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
Z = (np.sin(X) / X) * (np.sin(Y) / Y)
plt.imshow(Z)

plt.show()
