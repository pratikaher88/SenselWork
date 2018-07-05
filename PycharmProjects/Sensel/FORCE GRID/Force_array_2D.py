import numpy as np
from SenselUse import sensel
import threading
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


enter_pressed = False

plt.figure(figsize=(15, 7))

# my_cmap = plt.cm.RdBu(np.arange(plt.cm.RdBu.N))
# my_cmap[:,0:3] *= 0.5
# my_cmap = ListedColormap(my_cmap)

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
    error = sensel.setFrameContent(handle, sensel.FRAME_CONTENT_PRESSURE_MASK)
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

    force1Darray = []
    for n in range(info.num_rows * info.num_cols):
        force1Darray.append(frame.force_array[n])

    B = np.reshape(force1Darray, (-1, 185))

    B=B*10

    print(B.sum())

    # C = np.where(B > 0, 1, 0)
    # print(C)

    # ax = sns.heatmap(B, linewidth=0.5)
    # plt.imshow(B, cmap='RdPu', vmin=0 , vmax=200,interpolation='nearest')

    plt.imshow(B, cmap='hot', vmin=0 , vmax=200,interpolation='nearest')
    plt.pause(0.0001)
    plt.cla()

    # for n in range(info.num_rows):
    #     print(frame.force_array[n])

    # for n in range(info.num_rows*info.num_cols):
    #     if frame.force_array[n]>0:
    #         print("Force :",n,frame.force_array[n])
    #     total_force += frame.force_array[n]
    # print("Total Force: "+str(total_force))


def closeSensel(frame):
    error = sensel.freeFrameData(handle, frame)
    error = sensel.stopScanning(handle)
    error = sensel.close(handle)


if __name__ == "__main__":

    handle = openSensel()
    if handle != None:

        (error, info) = sensel.getSensorInfo(handle)
        frame = initFrame()
        t = threading.Thread(target=waitForEnter)
        t.start()
        while (enter_pressed == False):
            scanFrames(frame, info)

        closeSensel(frame)
