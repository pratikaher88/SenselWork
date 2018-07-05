#!/usr/bin/env python

##########################################################################
# MIT License
#
# Copyright (c) 2013-2017 Sensel, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
# to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
##########################################################################

import sys
from SenselUse import sensel,sensel_register_map
import binascii
import threading

import matplotlib.pyplot as plt


global enter_pressed

X=[]
Y=[]
F=[]


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

    # total_force = 0.0
    # for n in range(info.num_rows * info.num_cols):
    #     total_force += frame.force_array[n]
    # print("Total Force: " + str(total_force))

    if frame.n_contacts > 0:
        print("\nNum Contacts: ", frame.n_contacts)

        for n in range(frame.n_contacts):
            c = frame.contacts[n]
            print("Contact ID: ", c.id)
            print("X_pos",c.x_pos)
            X.append(c.x_pos)
            Y.append(c.y_pos)
            print("Y_pos",c.y_pos)

            total_force = 0.0
            for n in range(info.num_rows * info.num_cols):
                total_force += frame.force_array[n]

            print("Total Force", total_force)

            if total_force<100:
                F.append('yellow')
            elif total_force<500:
                F.append('blue')
            elif total_force<1500:
                F.append('green')
            elif total_force<2500:
                F.append('red')



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

    handle = openSensel()
    if handle != None:
        (error, info) = sensel.getSensorInfo(handle)
        frame = initFrame()

        t = threading.Thread(target=waitForEnter)
        t.start()
        while (enter_pressed == False):
            scanFrames(frame, info)
        closeSensel(frame)
        # plt.figure(figsize=(230, 130))
        # plt.scatter(X,Y)
        # plt.show()
        plt.xlim(0, 230)
        plt.ylim(0, 130)
        plt.scatter(X, Y)
        plt.gca().invert_yaxis()

        plt.show()

        print(X)
        print(Y)


