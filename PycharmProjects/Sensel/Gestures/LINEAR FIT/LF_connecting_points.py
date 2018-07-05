import matplotlib.pyplot as plt
import numpy

# hl, = plt.plot([], [], linestyle='None')
import scipy.optimize as opt

from SenselUse import sensel,sensel_register_map
import threading
from scipy import spatial

from matplotlib import style
import numpy as np
from scipy.optimize import curve_fit
import statistics
style.use('fivethirtyeight')
points_seen_till_now = []

import time

global enter_pressed

hl, = plt.plot([], [], linestyle='None')

def waitForEnter():
    global enter_pressed
    input("Press Enter to exit...")
    enter_pressed = True
    return

def func(x, a, b):
    return a*x + b

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

            plt.subplot(2, 1, 1)
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
                    # print("XY", hl.get_xdata(), hl.get_ydata())
                    # print("STDY", statistics.stdev(hl.get_ydata()))
                    # print("STDX", statistics.stdev(hl.get_xdata()))

                    # if len(hl.get_data()) > 5:
                        # plt.scatter(hl.get_xdata(), hl.get_ydata())
                    # popt, pcov = curve_fit(func, hl.get_xdata(), hl.get_ydata())
                    # plt.figure(300)
                    # plt.xlim(0, 230)
                    # plt.ylim(0, 130)
                    # plt.gca().invert_yaxis()
                    # plt.plot(hl.get_xdata(), func(hl.get_xdata(), *popt), 'r-')
                    # plt.pause(0.0001)

                    xdata=np.delete(np.array(hl.get_xdata()),0)
                    ydata=np.delete(np.array(hl.get_ydata()),0)

                    print("START POINT",xdata[0],ydata[0])
                    print("END POINT",xdata[len(xdata)-1],ydata[len(ydata)-1])

                    print("PONITS SEEN BEFORE")

                    for point in points_seen_till_now:
                        print(point)


                    if len(points_seen_till_now)>1:
                        tree = spatial.KDTree(points_seen_till_now)
                        print(hl.get_xdata())
                        print(hl.get_ydata())
                        # print("QUERY",tree.query((xdata[len(xdata)-1],ydata[len(ydata)-1])))
                        querystart=tree.query((xdata[0],ydata[0]))
                        print("POINT TO BE COMPARED WITH START",xdata[0],ydata[0])
                        print("QUERY START POINT",querystart[0],points_seen_till_now[querystart[1]])
                        if querystart[0]<40:
                            print(xdata[0])
                            xdata[0]=points_seen_till_now[querystart[1]][0]
                            print(points_seen_till_now[querystart[1]][0])
                            print(ydata[0])
                            ydata[0]=points_seen_till_now[querystart[1]][1]
                            print(points_seen_till_now[querystart[1]][1])

                        queryend=tree.query((xdata[len(xdata)-1],ydata[len(ydata)-1]))
                        print("POINT TO BE COMPARED WITH END", xdata[len(xdata)-1], xdata[len(xdata)-1])
                        print("QUERY END POINT", queryend[0], points_seen_till_now[queryend[1]])
                        if queryend[0] < 40:
                            xdata[len(xdata)-1] = points_seen_till_now[queryend[1]][0]
                            ydata[len(xdata)-1] = points_seen_till_now[queryend[1]][1]


                    points_seen_till_now.append((xdata[0],ydata[0]))
                    points_seen_till_now.append((xdata[len(xdata)-1],ydata[len(ydata)-1]))

                    # print("PONITS SEEN AFTER", points_seen_till_now)

                    plt.subplot(2, 1, 2)
                    plt.xlim(0, 230)
                    plt.ylim(0, 130)

                    plt.gca().invert_yaxis()
                    plt.plot([xdata[0], xdata[len(xdata)-1]], [ydata[0], ydata[len(ydata)-1]], 'k-')

                    # optimizedParameters, pcov = opt.curve_fit(func, xdata, ydata)

                    # plt.figure(2)
                    # plt.xlim(0, 230)
                    # plt.ylim(0, 130)

                    # plt.gca().invert_yaxis()
                    # plt.plot(xdata, func(xdata, *optimizedParameters), label="fit")

                    hl.set_xdata(0)
                    hl.set_ydata(0)


                    # plt.subplot(2,1,1)
                    # plt.cla()

            plt.pause(0.0001)

            if c.state == sensel.CONTACT_START:
                sensel.setLEDBrightness(handle, c.id, 100)

            elif c.state == sensel.CONTACT_END:
                sensel.setLEDBrightness(handle, c.id, 0)


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


