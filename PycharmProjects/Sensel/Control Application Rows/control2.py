import numpy
from SenselUse import sensel,sensel_register_map
import threading
import pymouse
m = pymouse.PyMouse()
import numpy as np
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

        # self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid)
        panel.SetSizer(sizer)


        # wx.PostEvent(self.GetEventHandler(), gridlib.EVT_GRID_SELECT_CELL)


    # def OnSelectCell(self, evt):
    #     if evt.Selecting():
    #         msg = 'Selected'
    #     else:
    #         msg = 'Deselected'
    #     print(
    #     "OnSelectCell: %s (%d,%d) %s\n" % (msg, evt.GetRow(),
    #                                        evt.GetCol(), evt.GetPosition()))

global enter_pressed

def waitForEnter():
    global enter_pressed
    input("Press Enter to exit...")
    enter_pressed = True
    return

def openSensel():
    handle = None
    (error, device_list) = sensel.getDeviceList()
    if device_list.num_devices != 0:
        (error, handle) = sensel.openDeviceByID(device_list.devices[0].idx)
    return handle

def initFrame():
    error = sensel.setFrameContent(handle, sensel.FRAME_CONTENT_PRESSURE_MASK | sensel.FRAME_CONTENT_CONTACTS_MASK)
    sensel.setContactsMask(handle, sensel.CONTACT_MASK_ELLIPSE | sensel.CONTACT_MASK_BOUNDING_BOX)
    sensel.writeReg(handle, sensel_register_map.SENSEL_REG_BASELINE_DYNAMIC_ENABLED, 1, [0])

    (error, frame) = sensel.allocateFrameData(handle)
    error = sensel.startScanning(handle)
    return frame

def scanFrames(frame, info):
    error = sensel.readSensor(handle)
    (error, num_frames) = sensel.getNumAvailableFrames(handle)

    for i in range(num_frames):
        error = sensel.getFrame(handle, frame)
        printFrame(frame, info)

def printFrame(frame, info):

    if frame.n_contacts > 0:
        print("\nNum Contacts: ", frame.n_contacts)
        for n in range(frame.n_contacts):
            c = frame.contacts[n]
            print(c.id)
            print(c.x_pos,c.y_pos)
            print("Force at contact point",c.total_force)

def closeSensel(frame):
    error = sensel.freeFrameData(handle, frame)
    error = sensel.stopScanning(handle)
    error = sensel.close(handle)

if __name__ == "__main__":
    global enter_pressed
    enter_pressed = False

    handle = openSensel()
    if handle != None:
        (error, info) = sensel.getSensorInfo(handle)
        frame = initFrame()
        t = threading.Thread(target=waitForEnter)
        t.start()

        while (enter_pressed == False):
            scanFrames(frame, info)
        closeSensel(frame)




