import matplotlib.pyplot as plt

fig=plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_xlim(0, 230)
ax.set_ylim(0, 130)
ax.invert_yaxis()

colLabels=("Structure", "Energy", "Density","Density","Density","Density")
clust_data=[(1,2,3,5),(1,2,3,5),(1,2,3,5),(1,2,3,5),(1,2,3,5),(1,2,3,5),(1,2,3,5)]

the_table = ax.table(cellText=clust_data,
          colLabels=colLabels,
          loc='center')

print(len(clust_data))

cellDict=the_table.get_celld()

# for key,val in cellDict.items():
#     # print(key.get_width())
#     print(val.get_height())

# print(the_table._get_grid_bbox(c))

for key,val in the_table.get_celld().items():
    print(key,val)


c = the_table.get_celld()[(1, 1)]
c.set_color('blue')

plt.show()