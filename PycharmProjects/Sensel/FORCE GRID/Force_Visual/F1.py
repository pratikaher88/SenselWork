import pylab as pl
from matplotlib import cm
import numpy as np
from scipy import interpolate
from scipy import ndimage

FR = np.array([[0.763, 0.762, 0.954, 0.000, 0.835, 0.000],
               [0.000, 1.052, 1.080, 1.176, 0.864, 0.811],
               [1.179, 1.148, 1.368, 0.000, 1.147, 0.000],
               [0.000, 1.279, 1.315, 1.434, 1.031, 0.880],
               [1.176, 1.134, 1.355, 0.000, 1.131, 0.000],
               [0.000, 1.008, 1.045, 1.092, 0.840, 0.724],
               [0.672, 0.682, 0.755, 0.708, 0.643, 0.000]])

X, Y = np.mgrid[0:1:7j, 0:1:6j]

fig, axes = pl.subplots(1, 3, figsize=(15, 4))
c1 = axes[0].contourf(X, Y, FR)
pl.colorbar(c1, ax=axes[0])

# tmp = np.repeat(np.repeat(FR, 10, axis=1), 10, axis=0)
# x, y = np.mgrid[0:1:70j, 0:1:60j]
# c2 = axes[1].contourf(x, y, ndimage.gaussian_filter(tmp, 3), levels=c1.levels)
# pl.colorbar(c2, ax=axes[1]);
#
# rbf = interpolate.Rbf(X.ravel(), Y.ravel(), FR.ravel(), smooth=0.000001)
#
# X2, Y2 = np.mgrid[0:1:70j, 0:1:60j]
#
# c3 = pl.contourf(X2, Y2, rbf(X2, Y2))
# pl.colorbar(c3, ax=axes[2]);

pl.show()