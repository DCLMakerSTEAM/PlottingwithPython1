import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
Z = (np.sin(X) / X) * (np.sin(Y) / Y)
fig, ax = plt.subplots(subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z, cmap="viridis")

plt.show()
