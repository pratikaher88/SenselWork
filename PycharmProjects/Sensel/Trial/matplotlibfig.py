import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py


np.random.seed(5)
# x = np.arange(1, 101)

x=[  0.        ,  31.1328125  , 34.76953125 , 59.09765625  ,47.984375   , 71.7265625,
  57.34765625 , 82.484375  ,  64.51171875,  91.25390625 , 69.45703125,
  96.0546875  , 69.9453125  , 97.10546875]
# y = 20 + 3 * x + np.random.normal(0, 60, 100)

y=[   0.     ,     112.0859375  , 107.49609375 , 107.9453125  ,  79.62109375,
   85.07421875  , 55.83203125 ,  62.28515625 ,  37.65625   ,   44.046875,
   24.02734375  , 30.46484375   ,22.75    ,     28.54296875]
# plt.figure(figsize=(230,130))


plt.scatter(x, y)
plt.xlim(0, 230)
plt.ylim(0,130)
plt.gca().invert_yaxis()

plt.show()
# print(x)
# print(y)




