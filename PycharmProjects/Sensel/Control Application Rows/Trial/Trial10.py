import matplotlib.pyplot as plt
import numpy as np

def onclick(event):
    print("EVENT CALLED")

    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))

plt.figure(figsize=(15,7))
ax = plt.gca()
fig = plt.gcf()# Make a 9x9 grid...
nrows, ncols = 10,20
image = np.zeros(nrows*ncols)

# Reshape things into a 9x9 grid.
image = image.reshape((nrows, ncols))

# row_labels = range(nrows)
# col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# plt.xticks(range(ncols), col_labels)
# plt.yticks(range(nrows), row_labels)
# plt.grid(True)

fig.canvas.mpl_connect('button_press_event', onclick)

image[2:6, 4:8] = 7

ax.matshow(image)

plt.show()