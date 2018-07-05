import wx

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size=(600, 300))
        self.panel = wx.Panel(self,-1)
        #self.panel.Bind(wx.EVT_MOTION,  self.OnMove)
        my_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
        my_apple = wx.RadioButton(self.panel, -1, "Apple")
        my_mango = wx.RadioButton(self.panel, -1, "Mango")
        my_banana = wx.RadioButton(self.panel, -1, "Banana")
        my_orange = wx.CheckBox(self.panel, -1, "Orange", (20,250), (160,-1))
        my_boxsizer.Add(my_apple, 0, wx.ALL|wx.EXPAND, 5)
        my_boxsizer.Add(my_mango, 0, wx.ALL|wx.EXPAND, 5)
        my_boxsizer.Add(my_banana, 0, wx.ALL|wx.EXPAND, 5)
        my_boxsizer.Add(my_orange, 0, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(my_boxsizer)
        # my_banana.SetValue(True)
        my_orange.SetValue(True)

        evt = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, my_banana.GetId())
        wx.PostEvent(self, evt)

        self.Show()


app = wx.App()
frame = MyFrame()
app.MainLoop()