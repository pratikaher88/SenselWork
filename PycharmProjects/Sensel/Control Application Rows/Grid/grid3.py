import wx
import wx.grid as gridlib


########################################################################
class MyGrid(gridlib.Grid):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        gridlib.Grid.__init__(self, parent)
        self.CreateGrid(12, 8)

        # test all the events

        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick)
        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnCellRightClick)
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnCellLeftDClick)
        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_DCLICK, self.OnCellRightDClick)

        self.Bind(gridlib.EVT_GRID_ROW_SIZE, self.OnRowSize)
        self.Bind(gridlib.EVT_GRID_COL_SIZE, self.OnColSize)

        self.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)
        self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)


    def OnCellLeftClick(self, evt):
        print("OnCellLeftClick: (%d,%d) %s\n" % (evt.GetRow(),
                                           evt.GetCol(),
                                           evt.GetPosition()))


    def OnCellRightClick(self, evt):
        print(
        "OnCellRightClick: (%d,%d) %s\n" % (evt.GetRow(),
                                            evt.GetCol(),
                                            evt.GetPosition()))


    def OnCellLeftDClick(self, evt):
        print(
        "OnCellLeftDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                            evt.GetCol(),
                                            evt.GetPosition()))


    def OnCellRightDClick(self, evt):
        print(
        "OnCellRightDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                             evt.GetCol(),
                                             evt.GetPosition()))

    def OnRowSize(self, evt):
        print(
        "OnRowSize: row %d, %s\n" % (evt.GetRowOrCol(),
                                     evt.GetPosition()))

    def OnColSize(self, evt):
        print(
        "OnColSize: col %d, %s\n" % (evt.GetRowOrCol(),
                                     evt.GetPosition()))

    def OnRangeSelect(self, evt):
        if evt.Selecting():
            msg = 'Selected'
        else:
            msg = 'Deselected'
        print(
        "OnRangeSelect: %s  top-left %s, bottom-right %s\n" % (msg, evt.GetTopLeftCoords(),
                                                               evt.GetBottomRightCoords()))


    def OnSelectCell(self, evt):
        if evt.Selecting():
            msg = 'Selected'
        else:
            msg = 'Deselected'
        print(
        "OnSelectCell: %s (%d,%d) %s\n" % (msg, evt.GetRow(),
                                           evt.GetCol(), evt.GetPosition()))

        # Another way to stay in a cell that has a bad value...
        row = self.GetGridCursorRow()
        col = self.GetGridCursorCol()

        if self.IsCellEditControlEnabled():
            self.HideCellEditControl()
            self.DisableCellEditControl()

        value = self.GetCellValue(row, col)

        if value == 'no good 2':
            return  # cancels the cell selection



########################################################################
class MyForm(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="An Eventful Grid")
        panel = wx.Panel(self)

        myGrid = MyGrid(panel)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    frame = MyForm().Show()
    app.MainLoop()