import sys
from SenselUse import sensel
import binascii
import threading

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
    error = sensel.setFrameContent(handle, sensel.FRAME_CONTENT_CONTACTS_MASK)
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

    # print("Contact BIt MASK",frame.content_bit_mask)
    # print("Lost Frame Contact",frame.lost_frame_count)
    # print("Labels array",frame.labels_array[1])
    # print("AccelData",frame.accel_data[0])

    for n in range(info.num_rows*info.num_cols):
        print(frame.labels_array[n])

    print('--------------')


    # if frame.n_contacts > 0:
    #     print("\nNum Contacts: ", frame.n_contacts)
    #     for n in range(frame.n_contacts):
    #         c = frame.contacts[n]



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

