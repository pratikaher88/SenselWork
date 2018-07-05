import matplotlib.pyplot as plt
left, width = 0.1, 0.6
bottom, height = 0.1, 0.8
left_table = left+width+0.1
table_width = 0.15
table_height = width/2.

rect_table1 = [left_table, table_height+bottom , table_width, table_height]
rect_table2 = [left_table, bottom, table_width, table_height]

axTable1 = plt.axes(rect_table1, frameon =False)
axTable2 = plt.axes(rect_table2, frameon =False)
axTable1.axes.get_xaxis().set_visible(False)
axTable2.axes.get_xaxis().set_visible(False)
axTable1.axes.get_yaxis().set_visible(False)
axTable2.axes.get_yaxis().set_visible(False)

axTable1.table(cellText=[[1,1],[2,2]], loc='upper center',
               rowLabels=['row1','row2'], colLabels=['col1','col2'])
axTable2.table(cellText=[[3,3],[4,4]], loc='upper center',
               rowLabels=['row1','row2'], colLabels=['col1','col2'])

plt.show()