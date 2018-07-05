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
hover=[]

def a2cell(rows,cols,x, y):
    single_cell_width, single_cell_height = 230 / cols, 130 / rows
    row_values=[]
    col_values = []
    for i in range(cols+1):
        row_values.append(i*single_cell_width)
    for i in range(rows+1):
        col_values.append(i*single_cell_height)

    # print(row_values)
    # print(col_values)

    for col in col_values:
        for row in row_values:
            if row>x and col>y:
                print(row,col)
                cell_list.append((col_values.index(col)-1,row_values.index(row)-1))
                print(col_values.index(col)-1,row_values.index(row)-1)
                return

def a2cellhover(rows,cols,x, y):
    single_cell_width, single_cell_height = 230 / cols, 130 / rows
    row_values=[]
    col_values = []
    for i in range(cols+1):
        row_values.append(i*single_cell_width)
    for i in range(rows+1):
        col_values.append(i*single_cell_height)

    # print(row_values)
    # print(col_values)

    for col in col_values:
        for row in row_values:
            if row>x and col>y:
                print(row,col)
                hover.append((col_values.index(col)-1,row_values.index(row)-1))
                print(col_values.index(col)-1,row_values.index(row)-1)
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

def appendtocell(x, y):
    #     compx = 220
    #     compy = 120
    #     m = 29
    #     n = 4
    #
    if x > 175 and y > 77:
        cell_list.append((7, 3))
    elif x > 175 and y > 74:
        cell_list.append((6, 3))
    elif x > 175 and y > 71:
        cell_list.append((5, 3))
    elif x > 175 and y > 67:
        cell_list.append((4, 3))
    elif x > 175 and y > 64:
        cell_list.append((3, 3))
    elif x > 175 and y > 58:
        cell_list.append((2, 3))
    elif x > 175 and y > 54:
        cell_list.append((1, 3))

    elif x > 105 and y > 77:
        cell_list.append((7, 2))
    elif x > 105 and y > 74:
        cell_list.append((6, 2))
    elif x > 105 and y > 71:
        cell_list.append((5, 2))
    elif x > 105 and y > 67:
        cell_list.append((4, 2))
    elif x > 105 and y > 64:
        cell_list.append((3, 2))
    elif x > 105 and y > 58:
        cell_list.append((2, 2))
    elif x > 105 and y > 54:
        cell_list.append((1, 2))

    elif x > 60 and y > 77:
        cell_list.append((7, 1))
    elif x > 60 and y > 74:
        cell_list.append((6, 1))
    elif x > 60 and y > 71:
        cell_list.append((5, 1))
    elif x > 60 and y > 67:
        cell_list.append((4, 1))
    elif x > 60 and y > 64:
        cell_list.append((3, 1))
    elif x > 60 and y > 58:
        cell_list.append((2, 1))
    elif x > 60 and y > 54:
        cell_list.append((1, 1))

    elif x > 3 and y > 77:
        cell_list.append((7, 0))
    elif x > 3 and y > 74:
        cell_list.append((6, 0))
    elif x > 3 and y > 71:
        cell_list.append((5, 0))
    elif x > 3 and y > 67:
        cell_list.append((4, 0))
    elif x > 3 and y > 64:
        cell_list.append((3, 0))
    elif x > 3 and y > 58:
        cell_list.append((2, 0))
    elif x > 3 and y > 54:
        cell_list.append((1, 0))

def printFrame(frame, info):
    cell_list.clear()

    if frame.n_contacts > 0:

        print("\nNum Contacts: ", frame.n_contacts)

        # contacts_dict=defaultdict(list)
        contacts_list = []
        patches=[]

        for n in range(frame.n_contacts):
            c = frame.contacts[n]

            print(c.id)
            print(c.x_pos, c.y_pos)
            # print("Force at contact point", c.total_force)
            # print(c.orientation)

            if c.total_force > 500:
                # appendtocell(c.x_pos, c.y_pos)
                a2cell(rows,cols,c.x_pos, c.y_pos)

            a2cellhover(rows,cols,c.x_pos, c.y_pos)

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

                print("HOVER",hover)

                for val in hover:
                    col = the_table.get_celld()[val]
                    col.set_facecolor('g')

                new_cell_list = []

                for value in Counter(cell_list).most_common(2):
                    new_cell_list.append(value[0])

                print("NEWCELLLIST",new_cell_list)

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
                    if ((new_cell_list[0][0]-new_cell_list[1][0])/(new_cell_list[0][1]-new_cell_list[1][1]))==1:
                        print("Diagonal")

                        for i,j in zip(range(new_cell_list[1][0] + 1, new_cell_list[0][0]),range(new_cell_list[1][1] + 1, new_cell_list[0][0])):
                            print(i,j)
                            selected_cell_list.append((i,j))
                            col = the_table.get_celld()[i, j]
                            col.set_facecolor('blue')
                except:
                    pass


                if c.total_force>1000:

                    try:
                        if ((new_cell_list[0][0]-new_cell_list[1][0])/(new_cell_list[0][1]-new_cell_list[1][1]))==1:
                            for i in range(new_cell_list[1][0] , new_cell_list[0][0]+1):
                                for j in range(new_cell_list[1][1] , new_cell_list[0][1]+1):
                                    print("IJ",i,j)
                                    selected_cell_list.append((i, j))
                                    col = the_table.get_celld()[i, j]
                                    col.set_facecolor('red')

                    except:
                        pass

                if c.state == 3:
                    [p.remove() for p in reversed(ax.patches)]





