import numpy as np
import scipy as sp
import scipy.interpolate
import matplotlib.pyplot as plt

# Generate some random data
y = (np.random.random(10) - 0.5).cumsum()
x = np.arange(y.size)


def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate some data, you don't have to do this, as you already have your data
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise

# Interpolate the data using a cubic spline to "new_length" samples
new_length = 50
new_x = np.linspace(xdata.min(), xdata.max(), new_length)
new_y = sp.interpolate.interp1d(xdata, ydata, kind='cubic')(new_x)

# Plot the results
plt.figure()
plt.subplot(2,1,1)
plt.plot(xdata, ydata, 'bo-')
plt.title('Using 1D Cubic Spline Interpolation')

plt.subplot(2,1,2)
plt.plot(new_x, new_y, 'ro-')

plt.show()