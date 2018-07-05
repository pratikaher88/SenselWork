from collections import defaultdict

import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Ellipse,Rectangle

from SenselUse import sensel,sensel_register_map
import threading

from matplotlib import style
import numpy as np
import math
style.use('fivethirtyeight')


nrows, ncols = 150,250
image = np.zeros(nrows*ncols)
image = image.reshape((nrows, ncols))

plt.figure(0, figsize=(15, 7))
fig=plt.gcf()
ax = plt.gca()
ax.set_xlim(0, 230)
ax.set_ylim(0, 130)
ax.invert_yaxis()
ax.matshow(image)
plt.grid(False)
points_to_selected=[]

def onclick(x,y):
    points_to_selected.append((x,y))

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
        contacts_list = []
        for n in range(frame.n_contacts):
            c = frame.contacts[n]
            contacts_list.append((c.x_pos,c.y_pos,c.total_force))
            if len(contacts_list)==frame.n_contacts:
                print(contacts_list)
                for r in contacts_list:

                    ax.add_patch(Ellipse(xy=(r[0], r[1]), width=c.major_axis, height=c.minor_axis, edgecolor='y',
                                         facecolor='none',
                                         angle=c.orientation))
                    if r[2]>1500:
                        print("POINT FIXED")
                        onclick(r[0],r[1])

                if c.state==3:
                    [p.remove() for p in reversed(ax.patches)]

                plt.pause(0.001)

            [p.remove() for p in reversed(ax.patches)]

        print(points_to_selected)
        if len(points_to_selected)>2:
            image[math.floor(points_to_selected[0][0]):math.floor(points_to_selected[0][0])+30, math.floor(points_to_selected[0][0]):math.floor(points_to_selected[0][0])+30] = 7
            # image[100:120, 50:80] = 7
            ax.matshow(image)

        print("POINTS TO BE SELECTED",points_to_selected)

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
