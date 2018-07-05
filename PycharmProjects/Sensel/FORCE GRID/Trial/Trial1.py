import numpy
import matplotlib.pyplot as plt
# x = numpy.arange(0, 1, 0.05)
# y = numpy.power(x, 2)


fig= plt.subplots(num=None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')


plt.gca().set_xticks(numpy.arange(0, 185, 1))

plt.gca().set_yticks(numpy.arange(0, 105, 1))

plt.grid()

plt.gca().axes.get_xaxis().set_ticklabels([])
plt.gca().axes.get_yaxis().set_ticklabels([])
# plt.plot(100,100,'ro')
plt.show()