
"""
==========================
Rotating 3D wireframe plot
==========================

A very simple 'animation' of a 3D plot.  See also rotate_axes3d_demo.
"""

from __future__ import print_function

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time


# Total Force 0.0
# XYXYX 120.0 40.0 125.0 50.0
# Contact ID:  4
# X_pos 58.578125
# Y_pos 24.41015625
# Force at contact point 58.125
# STATE 3
def generate(X, Y, phi):
    '''
    Generates Z data for the points in the X, Y meshgrid and parameter phi.
    '''
    R = 1 - np.sqrt(X**2 + Y**2)
    return np.cos(2 * np.pi * X + phi) * R


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make the X, Y meshgrid.
xs = np.linspace(120.0, 125.0, 50)
# bounding box
ys = np.linspace(40.0, 50.0, 50)


X, Y = np.meshgrid(xs, ys)

# Set the z axis limits so they aren't recalculated each frame.
ax.set_zlim(-1, 1)

# Begin plotting.
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    # If a line collection is already remove it before drawing.

    # Plot the new wireframe and pause briefly before continuing.
    Z = generate(X, Y, phi)
    print(Z)
    ax.xlim(0, 230)
    ax.ylim(0, 130)
    ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)

print('Average FPS: %f' % (100 / (time.time() - tstart)))