import matplotlib.pyplot as plt
import numpy

# hl, = plt.plot([], [], linestyle='None')

from SenselUse import sensel,sensel_register_map
import threading


from matplotlib import style
import numpy as np
from scipy.optimize import curve_fit
import statistics
style.use('fivethirtyeight')

import time

global enter_pressed

hl, = plt.plot([], [], linestyle='None')

def waitForEnter():
    global enter_pressed
    input("Press Enter to exit...")
    enter_pressed = True
    return

def func(x, a, b, c):
 return a * np.exp(-b * x) + c

def openSensel():
    handle = None
    (error, device_list) = sensel.getDeviceList()
    if device_list.num_devices != 0:
        (error, handle) = sensel.openDeviceByID(device_list.devices[0].idx)
    return handle


def initFrame():
    error = sensel.setFrameContent(handle, sensel.FRAME_CONTENT_PRESSURE_MASK | sensel.FRAME_CONTENT_CONTACTS_MASK)
    sensel.setContactsMask(handle, sensel.CONTACT_MASK_ELLIPSE | sensel.CONTACT_MASK_BOUNDING_BOX)
    # sensel.writeReg(handle, sensel_register_map.SENSEL_REG_BASELINE_DYNAMIC_ENABLED, 1, [0])

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
        print('xxxxxxxxxxxx')

        count=0

        for n in range(frame.n_contacts):
            print('------------')
            c = frame.contacts[n]
            plt.xlim(0, 230)
            plt.ylim(0, 130)
            plt.gca().invert_yaxis()
            print("Contact ID: ", c.id)
            print("X_pos",c.x_pos)
            print("Y_pos",c.y_pos)
            print("ID",c.id)
            print("State",c.state)

            total_force = 0.0
            for n in range(info.num_rows * info.num_cols):
                total_force += frame.force_array[n]

            hl.set_xdata(numpy.append(hl.get_xdata(), c.x_pos))
            hl.set_ydata(numpy.append(hl.get_ydata(), c.y_pos))

            plt.scatter(c.x_pos, c.y_pos, marker='o', color='b')


            # if(c.total_force<100):
            #     x=plt.scatter(c.x_pos, c.y_pos, marker='o', color='b')
            # elif(c.total_force<400):
            #     x=plt.scatter(c.x_pos, c.y_pos, marker='o', color='y')
            # elif (c.total_force < 600):
            #     x=plt.scatter(c.x_pos, c.y_pos, marker='o',color='g')
            # elif (c.total_force >600):
            #     x=plt.scatter(c.x_pos, c.y_pos, marker='o', color='r')

            plt.annotate(c.id+1,(c.x_pos,c.y_pos),size=8)

            # popt, pcov = curve_fit(func, hl.get_xdata(), hl.get_ydata(), bounds=(0, [3., 1., 0.5]))
            # plt.plot(hl.get_xdata(), func(xdata, *popt), 'g--',
            #          label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

            if c.state==3:
                count=count+1
                if count==frame.n_contacts:
                    print("XY", hl.get_xdata(), hl.get_ydata())
                    print("STD", statistics.stdev(hl.get_ydata()))
                    print("STD", statistics.stdev(hl.get_xdata()))

                    # if len(hl.get_data()) > 5:
                        # plt.scatter(hl.get_xdata(), hl.get_ydata())
                    # popt, pcov = curve_fit(func, hl.get_xdata(), hl.get_ydata())
                    # plt.figure(300)
                    # plt.xlim(0, 230)
                    # plt.ylim(0, 130)
                    # plt.gca().invert_yaxis()
                    # plt.plot(hl.get_xdata(), func(hl.get_xdata(), *popt), 'r-')
                    # plt.pause(0.0001)

                    hl.set_xdata(0)
                    hl.set_ydata(0)

                    # plt.figure(1)
                    plt.cla()

            plt.pause(0.0001)

            if c.state == sensel.CONTACT_START:
                sensel.setLEDBrightness(handle, c.id, 100)

            elif c.state == sensel.CONTACT_END:
                sensel.setLEDBrightness(handle, c.id, 0)


        # hl.set_xdata(0)
        # hl.set_ydata(0)


        # print("XY",hl.get_xdata(), hl.get_ydata())






def closeSensel(frame):
    error = sensel.freeFrameData(handle, frame)
    error = sensel.stopScanning(handle)
    error = sensel.close(handle)


if __name__ == "__main__":
    global enter_pressed
    enter_pressed = False



    # plt.show(block=False)

    handle = openSensel()
    if handle != None:
        (error, info) = sensel.getSensorInfo(handle)
        frame = initFrame()

        t = threading.Thread(target=waitForEnter)
        t.start()
        hl.set_xdata(0)
        hl.set_ydata(0)
        while (enter_pressed == False):
            scanFrames(frame, info)
        closeSensel(frame)

        plt.close()
        # plt.show()


