from collections import defaultdict, Counter

import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Ellipse, Rectangle

# hl, = plt.plot([], [])

from SenselUse import sensel, sensel_register_map
import threading

from matplotlib import style
import numpy as np
import numpy as np

fig = plt.figure(0, figsize=(15, 7))
ax = fig.add_subplot(111)
ax.invert_yaxis()

Hist=[]

style.use('fivethirtyeight')

global enter_pressed

def isSorted(x, key = lambda x: x):
    return all([key(x[i]) <= key(x[i + 1]) for i in range(len(x) - 1)])

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

            print("Orient",c.orientation)

            Hist.append(c.orientation)

        print(isSorted(Hist))

        if isSorted(Hist)==False:
            print("Direction Change")
            print("HIST",len(Hist))
            print("MEAN",np.mean(Hist))

            if np.mean(Hist)>0:
                print("Left Direction")
            elif np.mean(Hist)<0:
                print("Right Direction")

            if c.state==3:
                Hist.clear()

            # Hist.append(c.orientation)
            # plt.bar(np.arange(len(Hist)), Hist)
            # plt.pause(0.0001)
            # plt.cla()

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
