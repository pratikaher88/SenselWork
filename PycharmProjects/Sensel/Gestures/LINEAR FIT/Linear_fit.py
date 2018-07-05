import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

from scipy.optimize import curve_fit
# def func(x, a, b, c):
#  return a * np.exp(-b * x) + c
def func(x, a, b):
    return a*x + b


#
# xdata = np.linspace(0, 4, 50)
# y = func(xdata, 2.5, 1.3, 0.5)
# np.random.seed(1729)
# y_noise = 0.2 * np.random.normal(size=xdata.size)
# ydata = y + y_noise



# xdata=np.array([ 106.02734375 , 106.19921875 , 106.671875    ,109.07421875 , 110.69921875,
#   112.48046875 , 114.33984375  ,117.46875     ,119.12109375 , 119.6015625,
#   119.2109375  , 118.87109375  ,119.0078125  , 119.26953125 , 119.4375,
#   119.47265625 , 119.4609375 ])
#
# ydata=np.array( [ 116.6484375  , 114.46484375 , 109.515625  ,   92.703125   ,  80.6484375,
#    68.80859375  , 58.68359375  , 42.3046875   , 32.22265625  , 23.51953125,
#    16.4765625  ,  12.16015625 ,   9.453125    ,  8.15234375   , 7.21875,
#     7.55078125   , 7.7421875 ])


xdata= np.array([   48.51171875  , 59.3203125   , 77.4921875  , 100.25390625,
  119.8515625   ,139.8515625   ,169.2265625  , 188.5859375 ,  202.29296875,
  215.93359375 , 223.6640625  , 225.57421875] )
ydata=np.array([    93.24609375 , 86.7109375  , 77.4375   ,   66.69140625,
  57.97265625 , 49.828125  ,  36.87109375  ,27.77734375  ,21.63671875,
  16.9140625  , 14.74609375 , 14.49609375])



print(xdata,ydata)
plt.xlim(0, 230)
plt.ylim(0, 130)
plt.gca().invert_yaxis()

plt.scatter(xdata, ydata)
# popt, pcov = curve_fit(func, xdata, ydata)
# plt.plot(xdata, func(xdata, *popt), 'r-',
#          label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
#
# popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
# plt.plot(xdata, func(xdata, *popt), 'g--',
#  label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

optimizedParameters, pcov = opt.curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *optimizedParameters), label="fit")


plt.legend()
plt.show()