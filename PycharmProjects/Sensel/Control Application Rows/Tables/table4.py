import numpy as np
clust_data = [(1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5), (1, 2, 3, 5)]

rows,cols =np.shape(clust_data)[0],np.shape(clust_data)[1]

single_cell_width,single_cell_height=230/cols,130/rows

print(single_cell_width,single_cell_height)

cell_list=[]

def appendtocell(x, y):

    if x > single_cell_width*3 and y > single_cell_height*7:
        cell_list.append((7, 3))
    elif x > single_cell_width*3 and y > single_cell_height*6:
        cell_list.append((6, 3))
    elif x > single_cell_width*3 and y > single_cell_height*5:
        cell_list.append((5, 3))
    elif x > single_cell_width*3 and y > single_cell_height*4:
        cell_list.append((4, 3))
    elif x > single_cell_width*3 and y > single_cell_height*3:
        cell_list.append((3, 3))
    elif x > single_cell_width*3 and y > single_cell_height*2:
        cell_list.append((2, 3))
    elif x > single_cell_width*3 and y > single_cell_height*1:
        cell_list.append((1, 3))
        
    elif x > single_cell_width*2 and y > single_cell_height*7:
        cell_list.append((7, 2))
    elif x > single_cell_width*2 and y > single_cell_height*6:
        cell_list.append((6, 2))
    elif x > single_cell_width*2 and y > single_cell_height*5:
        cell_list.append((5, 2))
    elif x > single_cell_width*2 and y > single_cell_height*4:
        cell_list.append((4, 2))
    elif x > single_cell_width*2 and y > single_cell_height*3:
        cell_list.append((3, 2))
    elif x > single_cell_width*2 and y > single_cell_height*2:
        cell_list.append((2, 2))
    elif x > single_cell_width*2 and y > single_cell_height*1:
        cell_list.append((1, 2))

    elif x > single_cell_width and y > single_cell_height*7:
        cell_list.append((7, 1))
    elif x > single_cell_width and y > single_cell_height*6:
        cell_list.append((6, 1))
    elif x > single_cell_width and y > single_cell_height*5:
        cell_list.append((5, 1))
    elif x > single_cell_width and y > single_cell_height*4:
        cell_list.append((4, 1))
    elif x > single_cell_width and y > single_cell_height*3:
        cell_list.append((3, 1))
    elif x > single_cell_width and y > single_cell_height*2:
        cell_list.append((2, 1))
    elif x > single_cell_width and y > single_cell_height*1:
        cell_list.append((1, 1))

    elif x > 0 and y > single_cell_height*7:
        cell_list.append((7, 0))
    elif x > 0 and y > single_cell_height*6:
        cell_list.append((6, 0))
    elif x > 0 and y > single_cell_height*5:
        cell_list.append((5, 0))
    elif x > 0 and y > single_cell_height*4:
        cell_list.append((4, 0))
    elif x > 0 and y > single_cell_height*3:
        cell_list.append((3, 0))
    elif x > 0 and y > single_cell_height*2:
        cell_list.append((2, 0))
    elif x > 0 and y > single_cell_height:
        cell_list.append((1, 0))


def a2cell(rows,cols,x, y):
    single_cell_width, single_cell_height = 230 / cols, 130 / rows
    row_values=[]
    col_values = []
    for i in range(cols+1):
        row_values.append(i*single_cell_width)
    for i in range(rows+1):
        col_values.append(i*single_cell_height)

    print(row_values)
    print(col_values)

    for col in col_values:
        for row in row_values:
            if row>x and col>y:
                print(row,col)
                cell_list.append((row_values.index(row),col_values.index(col)))
                print(row_values.index(row),col_values.index(col))
                return

    # cell_list.append(())

print(rows,cols)
print(a2cell(rows,cols,200,100))
print(cell_list)





