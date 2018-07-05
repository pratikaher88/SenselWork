import matplotlib.pyplot as plt
import numpy as np
sin = np.sin
cos = np.cos
pi = np.pi

def delete(event):
    artist = event.artist
    artist.remove()
    event.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.linspace(0, 2*pi, 50)
y = 2*sin(x)
z = 2*cos(x)
line1, = ax.plot(x,y)
line2, = ax.plot(x,z)
for artist in [line1, line2]:
    artist.set_picker(5)
fig.canvas.mpl_connect('pick_event', delete)

plt.show()