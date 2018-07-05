# new_cell_list=[ (6, 3) , (3, 0)]

new_cell_list=[(6, 0), (3, 3)]

for i in range(new_cell_list[1][0], new_cell_list[0][0] + 1):
    for j in range(min(new_cell_list[1][1],new_cell_list[0][1]), max(new_cell_list[0][1],new_cell_list[1][1]) + 1):
        print("IJ", i, j)




# for i in range(max(new_cell_list[1][0], new_cell_list[0][0]),min(new_cell_list[1][0], new_cell_list[0][0])):
#     print(i)
# # print(new_cell_list[0][1],new_cell_list[1][1])
#
#
# # print(max(new_cell_list[1][0], new_cell_list[0][0]))
# #
# # print(min(new_cell_list[1][0], new_cell_list[0][0]))
#
#
# for val in range(min(new_cell_list[1][0], new_cell_list[0][0])+1,max(new_cell_list[1][0], new_cell_list[0][0])):
#     print(val)
#
# for val in range(min(new_cell_list[0][1], new_cell_list[1][1])+1,max(new_cell_list[0][1], new_cell_list[1][1])):
#     print(val)
#
#
# for i,j in zip(range(min(new_cell_list[1][0], new_cell_list[0][0])+1,max(new_cell_list[1][0], new_cell_list[0][0])),range(min(new_cell_list[0][1], new_cell_list[1][1])+1,max(new_cell_list[0][1], new_cell_list[1][1]))):
#     print(i,j)







# for i, j in zip(range(max(new_cell_list[1][0], new_cell_list[0][0]) + 1, min(new_cell_list[0][0], new_cell_list[1][0])),
#                 range(max(new_cell_list[1][1], new_cell_list[0][0]) + 1,
#                       min(new_cell_list[1][1], new_cell_list[0][0]))):
#     print(i, j)

