import matplotlib.pyplot as plt

from matplotlib.table import CustomCell
from matplotlib.widgets import TextBox

class EditableTable():
    def __init__(self, table):
        self.table = table
        self.ax = self.table.axes
        celld = table.get_celld()
        for key in celld.keys():
            if key[0] > 0 and key[1] > -1:
                cell = celld[key]
                cell.set_picker(True)
        self.canvas = self.table.get_figure().canvas
        self.cid = self.canvas.mpl_connect('pick_event', self.on_pick)
        self.tba = self.ax.figure.add_axes([0,0,.01,.01])
        self.tba.set_visible(False)
        self.tb = TextBox(self.tba, '', initial="")
        self.cid2 = self.tb.on_submit(self.on_submit)
        self.currentcell = celld[(1,0)]

    def on_pick(self, event):
        if isinstance(event.artist, CustomCell):
            # clear axes and delete textbox
            self.tba.clear()
            del self.tb
            # make textbox axes visible
            self.tba.set_visible(True)
            self.currentcell = event.artist
            # set position of textbox axes to the position of the current cell
            trans = self.ax.figure.transFigure.inverted()
            trans2 = self.ax.transAxes
            bbox = self.currentcell.get_bbox().transformed(trans2 + trans)
            self.tba.set_position(bbox.bounds)
            # create new Textbox with text of the current cell
            cell_text = self.currentcell.get_text().get_text()
            self.tb = TextBox(self.tba, '', initial=cell_text)
            self.cid2 = self.tb.on_submit(self.on_submit)

            self.canvas.draw()

    def on_submit(self, text):
        # write the text box' text back to the current cell
        self.currentcell.get_text().set_text(text)
        self.tba.set_visible(False)
        self.canvas.draw_idle()

column_labels = ('Length', 'Width', 'Height', 'Sold?')
row_labels = ['Ferrari', 'Porsche']
data = [[2.2, 1.6, 1.2, True],
        [2.1, 1.5, 1.4, False]]

fig, ax = plt.subplots()
table = ax.table(cellText=data, colLabels=column_labels, rowLabels=row_labels,
                 cellLoc='center', loc='bottom')

et = EditableTable(table)

ax.axis('off')

plt.show()