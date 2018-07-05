# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
# ax.plot(range(20))
# ax.axvspan(7, 17, alpha=0.5, color='red')
#
# plt.show()

import matplotlib.pyplot as plt


fig,ax= plt.subplots(figsize=(15,7))
# ax = fig.add_subplot(111, aspect='equal')
ax.set_xlim(0, 230)
ax.set_ylim(0, 130)
ax.invert_yaxis()

plt.axvspan(8, 17, ymin=0.5, ymax=0.6, alpha=0.5, color='red')

plt.rc('grid', linestyle="-", color='black')
# plt.scatter(x, y)
plt.grid(True)

plt.show()