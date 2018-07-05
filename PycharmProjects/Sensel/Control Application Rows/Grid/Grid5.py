import wx
import wx.grid as gridlib


########################################################################
class MyGrid(gridlib.Grid):

    #----------------------------------------------------------------------
    def __init__(self, parent, rows, cols):
        gridlib.Grid.__init__(self, parent)
        self.CreateGrid(rows, cols)


########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.grid_created = False

        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        col_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        rows_lbl = wx.StaticText(self, label="Rows", size=(30, -1))
        row_sizer.Add(rows_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.rows = wx.TextCtrl(self)
        row_sizer.Add(self.rows, 0, wx.ALL|wx.EXPAND, 5)

        cols_lbl = wx.StaticText(self, label="Cols", size=(30, -1))
        col_sizer.Add(cols_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.cols = wx.TextCtrl(self)
        col_sizer.Add(self.cols, 0, wx.ALL|wx.EXPAND, 5)

        grid_btn = wx.Button(self, label="Create Grid")
        grid_btn.Bind(wx.EVT_BUTTON, self.create_grid)

        self.main_sizer.Add(row_sizer, 0, wx.EXPAND)
        self.main_sizer.Add(col_sizer, 0, wx.EXPAND)
        self.main_sizer.Add(grid_btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(self.main_sizer)

    #----------------------------------------------------------------------
    def create_grid(self, event):
        """"""
        rows = int( self.rows.GetValue() )
        cols = int( self.cols.GetValue() )

        if self.grid_created:
            for child in self.main_sizer.GetChildren():
                widget = child.GetWindow()
                if isinstance(widget, gridlib.Grid):
                    self.main_sizer.Remove(widget)

        grid = MyGrid(self, rows, cols)
        self.main_sizer.Add(grid, 0, wx.ALL, 5)
        self.grid_created = True

        self.main_sizer.Layout()




########################################################################
class MyFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="grids", size=(800, 600))
        panel = MyPanel(self)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()