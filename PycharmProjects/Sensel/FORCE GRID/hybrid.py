from collections import defaultdict

import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Ellipse,Rectangle


# hl, = plt.plot([], [])

from SenselUse import sensel,sensel_register_map
import threading

from matplotlib import style
import numpy as np
plt.figure(figsize=(15, 7))

style.use('fivethirtyeight')

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
        # fig = plt.figure(0,figsize=(15,7))
        # ax = fig.add_subplot(111, aspect='equal')
        # ax.set_xlim(0, 230)
        # ax.set_ylim(0, 130)
        # ax.invert_yaxis()

        plt.subplot(2, 1, 1)
        force1Darray = []
        for n in range(info.num_rows * info.num_cols):
            force1Darray.append(frame.force_array[n])
        B = np.reshape(force1Darray, (-1, 185))

        # print(B)
        # ax = sns.heatmap(B, linewidth=0.5)
        plt.imshow(B, cmap='hot', interpolation='nearest')
        # plt.pause(0.0001)
        # plt.cla()

        # ax = fig.add_subplot(111, aspect='equal')
        # ax.set_xlim(0, 230)
        # ax.set_ylim(0, 130)
        # ax.invert_yaxis()

        # contacts_dict=defaultdict(list)
        contacts_list = []

        for n in range(frame.n_contacts):
            c = frame.contacts[n]

            print(c.id)
            print(c.x_pos,c.y_pos)
            print("Force at contact point",c.total_force)

            contacts_list.append((c.x_pos,c.y_pos,c.total_force))
            ax=plt.subplot(2, 1, 2)
            ax.set_xlim(0, 230)
            ax.set_ylim(0, 130)
            ax.invert_yaxis()

            if len(contacts_list)==frame.n_contacts:

                for r in contacts_list:

                    # for Opaque
                    # ax.add_patch(Ellipse(xy=(r[0], r[1]), width=c.major_axis, height=c.minor_axis, edgecolor='y',
                    #                      facecolor='none',
                    #                      angle=c.orientation))

                    if (r[2] < 100):
                        ax.add_patch(Ellipse(xy=(r[0], r[1]),alpha=1, width=c.major_axis, height=c.minor_axis, color='b',
                                             angle=c.orientation))

                    elif (r[2] < 400):
                        ax.add_patch(Ellipse(xy=(r[0], r[1]), width=c.major_axis, height=c.minor_axis ,color='y',
                                             angle=c.orientation))
                    elif (r[2] < 600):
                        ax.add_patch(Ellipse(xy=(r[0], r[1]), width=c.major_axis, height=c.minor_axis ,color='g',
                                             angle=c.orientation))
                    elif (r[2] > 600):
                        ax.add_patch(Ellipse(xy=(r[0], r[1]), width=c.major_axis, height=c.minor_axis ,color='r',
                                             angle=c.orientation))


                if c.state==3:
                    [p.remove() for p in reversed(ax.patches)]


                # ax.annotate((c.x_pos,c.y_pos), (c.x_pos, c.y_pos), size=8)
                plt.pause(0.0001)
                # plt.draw()


            [p.remove() for p in reversed(ax.patches)]

            print("STATE",c.state)

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




