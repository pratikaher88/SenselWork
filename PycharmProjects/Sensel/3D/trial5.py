from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

xx = np.linspace(-4, 4, 80)
yy = xx
x, y = np.meshgrid(xx, yy)

f = plt.figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')

def plot_3dG(c_, n_):
    ax = f.add_subplot(2, 2, n_, projection='3d', )
    r = np.sqrt(x**2 + y**2)
    print(r)
    c = c_
    r1 = abs(r + c)
    r2 = abs(r - c)
    print(r1)
    print(r2)
    heights = 0.5*(np.exp(-r1*r1) + np.exp(-r2*r2))
    print(heights)
    ax.plot_surface(x, y, heights, rstride=1, cstride=1, cmap=cm.coolwarm,
            linewidth=0, antialiased=False)
    plt.show()

c, n = 0, 1           #plot 1
plot_3dG(c, n)