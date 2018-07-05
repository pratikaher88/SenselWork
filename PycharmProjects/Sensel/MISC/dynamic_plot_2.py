import matplotlib.pyplot as plt
import numpy

# hl, = plt.plot([], [], linestyle='None')
hl, = plt.plot([], [])

from SenselUse import sensel,sensel_register_map
import threading


from matplotlib import style

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
    # sensel.writeReg(handle, sensel_register_map.SENSEL_REG_BASELINE_DYNAMIC_ENABLED, 1, [0])

    (error, frame) = sensel.allocateFrameData(handle)
    error = sensel.startScanning(handle)
    return frame

# def initFrameForContacts():
#     error = sensel.setFrameContent(handle, sensel.FRAME_CONTENT_CONTACTS_MASK)
#     (error, frame) = sensel.allocateFrameData(handle)
#     error = sensel.startScanning(handle)
#     return frame


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

    plt.gca().set_xticks(numpy.arange(0, 185, 1))
    plt.gca().set_yticks(numpy.arange(0, 105, 1))
    plt.grid()

    if frame.n_contacts > 0:
        print("\nNum Contacts: ", frame.n_contacts)

        for n in range(frame.n_contacts):
            c = frame.contacts[n]
            print("Contact ID: ", c.id)
            print("X_pos",c.x_pos)

            print("Y_pos",c.y_pos)


            total_force = 0.0
            for n in range(info.num_rows * info.num_cols):
                total_force += frame.force_array[n]

            print("Total Force", total_force)

            hl.set_xdata(numpy.append(hl.get_xdata(), c.x_pos))
            hl.set_ydata(numpy.append(hl.get_ydata(), c.y_pos))

            if(total_force<100):
                plt.scatter(c.x_pos, c.y_pos, marker='o', color='b')
            elif(total_force<500):
                plt.scatter(c.x_pos, c.y_pos, marker='o', color='y')
            elif (total_force < 1500):
                plt.scatter(c.x_pos, c.y_pos, marker='o',color='g')
            elif (total_force >2000):
                plt.scatter(c.x_pos, c.y_pos, marker='o', color='r')

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


    # plt.xlim(0, 230)
    # plt.ylim(0, 130)
    # # plt.scatter(X, Y)
    # plt.gca().invert_yaxis()

    # plt.show(block=False)

    handle = openSensel()
    if handle != None:
        (error, info) = sensel.getSensorInfo(handle)
        frame = initFrame()

        t = threading.Thread(target=waitForEnter)
        t.start()
        while (enter_pressed == False):
            scanFrames(frame, info)
        closeSensel(frame)

        # plt.show()



