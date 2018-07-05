from collections import Counter, defaultdict

cell_list=[(4, 0), (4, 0), (4, 0),(5,0), (4, 0),(4, 0),(4, 2), (4, 2), (4, 2), (4, 2), (4, 2), (4, 2) ]

# if len(set(cell_list)) == 2:
#     if cell_list[0][0] == cell_list[1][0]:
#         print(set(cell_list))
#         print(list(set(cell_list))[0][0], cell_list[1][1])
#         if list(set(cell_list))[0][0]==list(set(cell_list))[1][0]:
#             print("Draw Line")
#             print("FROM",list(set(cell_list))[1][1],"TO",list(set(cell_list))[0][1])
#             for i in range(list(set(cell_list))[1][1],list(set(cell_list))[0][1]+1):
                # the_table.get_celld()[(list(set(cell_list))[0][0], i)].set_color('blue')

        # for values in range(cell_list[0][1], cell_list[1][1]):
        #     print(cell_list[0][0], cell_list[1][1])


# print(set(cell_list))
#
# cell_list=list(set(cell_list))

# print(len(set(cell_list)))

print(cell_list)

# if len(set(cell_list)) == 2:
#     if cell_list[0][0] == cell_list[1][0]:
#         if list(set(cell_list))[0][0] == list(set(cell_list))[1][0]:
#             print("Draw Line")
#             print("FROM", list(set(cell_list))[1][1], "TO", list(set(cell_list))[0][1])
#             for i in range(list(set(cell_list))[1][1], list(set(cell_list))[0][1] + 1):
#                 print(i)
#                 # the_table.get_celld()[(list(set(cell_list))[0][0], i)].set_color('blue')


print(Counter(cell_list).most_common(2))

new_cell_list=[]

for value in Counter(cell_list).most_common(2):
    new_cell_list.append(value[0])
    # cell_list.append(value[0])

print(new_cell_list)

if new_cell_list[0][0] == new_cell_list[1][0]:
    if list(set(new_cell_list))[0][0] == list(set(new_cell_list))[1][0]:
        print("Draw Line")
        print("FROM", list(set(new_cell_list))[1][1], "TO", list(set(new_cell_list))[0][1])
        for i in range(list(set(new_cell_list))[1][1], list(set(new_cell_list))[0][1] + 1):
            print(i)
            # the_table.get_celld()[(list(set(new_cell_list))[0][0], i)].set_color('blue')


# inv_c = defaultdict(list)
# for k, v in Counter(cell_list).items():
#     inv_c[v].append(k)
# for value,count in Counter(cell_list):
#     print(value,count)




