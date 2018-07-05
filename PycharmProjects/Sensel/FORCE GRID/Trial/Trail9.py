import matplotlib.pyplot as plt
import numpy as np

# X, Y = np.meshgrid(range(100), range(100))
#
# # plt.imshow(Z,origin='lower',interpolation='nearest')
# # plt.show()
#
# plt.pcolormesh(X,Y)
# plt.show()
#
#
# plt.imshow(a, cmap='hot', interpolation='nearest')
# plt.show()

# plt.imshow(Z[20:40,30:70],origin='lower',interpolation='nearest')
# plt.show()
#
# plt.pcolormesh(X[20:40,30:70],Y[20:40,30:70])
# plt.show()


a = np.random.random((16, 16))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()
