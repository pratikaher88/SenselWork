# rect_lst = getListOfRandomRects(n='random', dim=img.shape[0:2])
#     [ax.add_patch(patches.Rectangle((r[0], r[1]), r[2], r[3],
#                                     linewidth=1, facecolor='none'))
#                  for r in rect_lst]
#
#     plt.pause(0.1)
#     plt.draw()
#     [p.remove() for p in reversed(ax.patches)]

import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={'xlim': [0,1],
                                   'ylim': [0,1]})


p1, = ax.plot(0.5, 0.5, 'bo') # creates a blue dot
p2, = ax.plot(0.5, 0.5, 'ro')

print(p2)
print(p1)
# p2.remove()

# plt.show()