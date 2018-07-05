import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(4,2))
colLabels = ["Name", "Number"]
data = [["Peter", 1], ["Sara", 1], ["John", 1]]
the_table = ax.table(cellText=data,
                     colLabels=colLabels,
                     loc='center')
c = the_table.get_celld()[(1, 1)]
c.set_color('blue')

def update(i):

    the_table._cells[(1, 1)]._text.set_text(str(i))
    the_table._cells[(2, 1)]._text.set_text(str(i*2))
    the_table._cells[(3, 1)]._text.set_text(str(i*3))


ani = FuncAnimation(fig, update, frames=20, interval=400)
plt.show()