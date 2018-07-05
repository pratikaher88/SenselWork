from collections import defaultdict, Counter

import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Ellipse, Rectangle

# hl, = plt.plot([], [])

from SenselUse import sensel, sensel_register_map
import threading

from matplotlib import style
import numpy as np

fig = plt.figure(0, figsize=(15, 7))
ax = fig.add_subplot(111)
# ax=plt.gca()
ax.set_xlim(0, 230)
ax.set_ylim(0, 130)
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
clust_data = [(1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5)]

rows,cols =np.shape(clust_data)[0],np.shape(clust_data)[1]

the_table = ax.table(cellText=clust_data,
                     loc='center',bbox=(0,0,1,1))

style.use('fivethirtyeight')

global enter_pressed

cell_list = []
hover_list=[]

def a2cell(rows,cols,x, y):
    single_cell_width, single_cell_height = 230 / cols, 130 / rows
    row_values=[]
    col_values = []
    for i in range(cols+1):
        row_values.append(i*single_cell_width)
    for i in range(rows+1):
        col_values.append(i*single_cell_height)

    for col in col_values:
        for row in row_values:
            if row>x and col>y:
                cell_list.append((col_values.index(col)-1,row_values.index(row)-1))
                return

def a2cellhover(rows,cols,x, y):
    single_cell_width, single_cell_height = 230 / cols, 130 / rows
    row_values=[]
    col_values = []
    for i in range(cols+1):
        row_values.append(i*single_cell_width)
    for i in range(rows+1):
        col_values.append(i*single_cell_height)

    for col in col_values:
        for row in row_values:
            if row>x and col>y:
                hover_list.append((col_values.index(col)-1,row_values.index(row)-1))
                return

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
    cell_list.clear()
    hover_list.clear()

    if frame.n_contacts > 0:

        print("\nNum Contacts: ", frame.n_contacts)

        contacts_list = []

        for n in range(frame.n_contacts):
            c = frame.contacts[n]

            print(c.x_pos, c.y_pos)

            if c.total_force > 500:
                # appendtocell(c.x_pos, c.y_pos)
                a2cell(rows,cols,c.x_pos, c.y_pos)

            a2cellhover(rows,cols,c.x_pos,c.y_pos)

            contacts_list.append((c.x_pos, c.y_pos, c.total_force))

            if len(contacts_list) == frame.n_contacts:

                for r in contacts_list:
                    # for Opaque
                    ax.add_patch(Ellipse(xy=(r[0], r[1]), width=c.major_axis, height=c.minor_axis, edgecolor='y',
                                         facecolor='none',
                                         angle=c.orientation))

                for val in cell_list:
                    col = the_table.get_celld()[val]
                    col.set_facecolor('blue')

                for val in hover_list:
                    col = the_table.get_celld()[val]
                    col.set_facecolor('green')

                new_cell_list = []

                for value in Counter(cell_list).most_common(2):
                    new_cell_list.append(value[0])

                new_cell_list = sorted(new_cell_list,reverse=True)
                print("NEWCELLLIST SORTED",new_cell_list)

                selected_cell_list=[]

                # Single Line Select
                try:
                    if new_cell_list[0][0] == new_cell_list[1][0]:
                        if list(set(new_cell_list))[0][0] == list(set(new_cell_list))[1][0]:
                            print("Draw Line")
                        for i in range(new_cell_list[1][1], new_cell_list[0][1] + 1):
                            selected_cell_list.append((new_cell_list[0][0], i))
                            col = the_table.get_celld()[new_cell_list[0][0], i]
                            col.set_facecolor('blue')

                except:
                    pass

                # diagonal select
                try:
                    if abs((new_cell_list[0][0]-new_cell_list[1][0])/(new_cell_list[0][1]-new_cell_list[1][1]))==1:
                        print("Diagonal")

                        col = the_table.get_celld()[new_cell_list[0][0], new_cell_list[0][1]]
                        col.set_facecolor('blue')
                        selected_cell_list.append((new_cell_list[0][0],new_cell_list[0][1]))
                        col = the_table.get_celld()[new_cell_list[1][0], new_cell_list[1][1]]
                        col.set_facecolor('blue')
                        selected_cell_list.append((new_cell_list[1][0], new_cell_list[1][1]))

                        if new_cell_list[1][1] > new_cell_list[0][1]:
                            for i, j in zip(range(new_cell_list[1][0] + 1, new_cell_list[0][0]),
                                            reversed(range(new_cell_list[0][1] + 1, new_cell_list[1][1]))):
                                selected_cell_list.append((i, j))
                                col = the_table.get_celld()[i, j]
                                col.set_facecolor('blue')
                        elif new_cell_list[1][1] < new_cell_list[0][1]:
                            for i, j in zip(range(new_cell_list[1][0] + 1, new_cell_list[0][0]),
                                            range(new_cell_list[1][1]+1,new_cell_list[0][1])):
                                selected_cell_list.append((i, j))
                                col = the_table.get_celld()[i, j]
                                col.set_facecolor('blue')
                except:
                    pass

                # BLOCK SELECT

                if c.total_force>1000:

                    try:
                        if abs((new_cell_list[0][0]-new_cell_list[1][0])/(new_cell_list[0][1]-new_cell_list[1][1]))==1:
                            print("BLOCK")

                            col = the_table.get_celld()[new_cell_list[0][0], new_cell_list[0][1]]
                            col.set_facecolor('red')
                            selected_cell_list.append((new_cell_list[0][0], new_cell_list[0][1]))
                            col = the_table.get_celld()[new_cell_list[1][0], new_cell_list[1][1]]
                            col.set_facecolor('red')
                            selected_cell_list.append((new_cell_list[1][0], new_cell_list[1][1]))

                            for i in range(new_cell_list[1][0], new_cell_list[0][0] + 1):
                                for j in range(min(new_cell_list[1][1], new_cell_list[0][1]),
                                               max(new_cell_list[0][1], new_cell_list[1][1]) + 1):
                                    selected_cell_list.append((i, j))
                                    col = the_table.get_celld()[i, j]
                                    col.set_facecolor('red')

                    except:
                        pass


                if c.state == 3:

                    for val in hover_list:
                        col = the_table.get_celld()[val]
                        col.set_facecolor('w')

                    [p.remove() for p in reversed(ax.patches)]

                plt.pause(0.0001)


                print("SELECTED CELL LIST", selected_cell_list)
                print("CELLLIST",cell_list)
                print("HOVERLIST",hover_list)

                for val in cell_list:
                        col = the_table.get_celld()[val]
                        col.set_facecolor('w')

                for val in hover_list:
                        col = the_table.get_celld()[val]
                        col.set_facecolor('w')

                for val in selected_cell_list:
                    col = the_table.get_celld()[val]
                    col.set_facecolor('w')


            [p.remove() for p in reversed(ax.patches)]

        [p.remove() for p in reversed(ax.patches)]


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
