import wx
import wx.grid as gridlib


class MyForm(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Grid Tutorial Two", size=(800, 600))
        panel = wx.Panel(self)
        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(20, 8)

        myGrid.SetCellValue(0, 0, "Hello")
        print(myGrid.GetCellValue(0, 0))

        myGrid.GetCellEditor(4,5)
        # for i in range(5):
        #     print(i)
        #     myGrid.SelectBlock(4,i,4,i)
        # myGrid.SelectBlock(1,1,1,1)

        myGrid.SetCellValue(1, 1, "I'm in red!")
        myGrid.SetCellTextColour(1, 1, wx.RED)

        myGrid.SetCellEditor(5, 0, gridlib.GridCellNumberEditor(1, 1000))
        myGrid.SetCellValue(5, 0, "123")

        myGrid.SetCellEditor(6, 0, gridlib.GridCellFloatEditor())
        myGrid.SetCellValue(6, 0, "123.34")
        myGrid.SetCellEditor(7, 0, gridlib.GridCellNumberEditor())

        self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)

        # wx.PyCommandEvent(gridlib.EVT_GRID_SELECT_CELL.typeId, self.GetId())

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid)
        panel.SetSizer(sizer)



        # wx.PostEvent(self.GetEventHandler(), gridlib.EVT_GRID_SELECT_CELL)


    def OnSelectCell(self, evt):
        if evt.Selecting():
            msg = 'Selected'
        else:
            msg = 'Deselected'
        print(
        "OnSelectCell: %s (%d,%d) %s\n" % (msg, evt.GetRow(),
                                           evt.GetCol(), evt.GetPosition()))

if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()