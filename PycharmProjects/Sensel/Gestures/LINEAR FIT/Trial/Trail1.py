# import numpy as np
# # def closest_node(node, nodes):
# #     nodes = np.asarray(nodes)
# #     print(a)
# #     dist_2 = np.sum((nodes - node)**2, axis=1)
# #     print(min(dist_2))
# #     print(dist_2)
# #     return np.argmin(dist_2)
# #
#
# def closest_node(node, nodes):
#     nodes = np.asarray(nodes)
#     deltas = nodes - node
#     dist_2 = np.einsum('ij,ij->i', deltas, deltas)
#     print(min(dist_2))
#     return np.argmin(dist_2)
#
#
# a=[(24.0703125, 30.1171875), (197.20703125, 43.55078125), (48.890625, 16.8984375), (78.51171875, 124.37109375), (71.3046875, 112.37890625), (173.8515625, 80.9375), (144.03515625, 32.00390625), (172.38671875, 108.1640625)]
#
# print(closest_node((21.0703125, 22.1171875), a))

from scipy import spatial
# airports = [(10,10),(20,20),(30,30),(40,40)]
a=[(24.0703125, 30.1171875), (197.20703125, 43.55078125), (48.890625, 16.8984375), (78.51171875, 124.37109375), (71.3046875, 112.37890625), (173.8515625, 80.9375), (144.03515625, 32.00390625), (172.38671875, 108.1640625)]


tree = spatial.KDTree(a)
print(tree.query([(197.0703125, 22.1171875)]))


