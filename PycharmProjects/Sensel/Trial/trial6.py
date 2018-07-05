import matplotlib.pyplot as plt;
import numpy as np;
import scipy.optimize as opt;
import threading



def Execute():
    # This is the function we are trying to fit to the data.
    def func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Generate some data, you don't have to do this, as you already have your data
    xdata = np.linspace(0, 4, 50)
    y = func(xdata, 2.5, 1.3, 0.5)
    y_noise = 0.2 * np.random.normal(size=xdata.size)
    ydata = y + y_noise

    ydata = (np.random.random(10) - 0.5).cumsum()
    xdata = np.arange(ydata.size)
    # N = 10
    # xdata = [0,1,2,3,4,5]
    # ydata = [0,1,2,3,4,5]

    print(xdata,ydata)

    # y = (np.random.random(10) - 0.5).cumsum()
    # x = np.arange(y.size)

    # Interpolate the data using a cubic spline to "new_length" samples
    # new_length = 50
    # new_x = np.linspace(x.min(), x.max(), new_length)
    # new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)

    print(len(xdata))
    print(len(ydata))

    # Plot the actual data
    plt.plot(xdata, ydata, ".", label="Data");

    # The actual curve fitting happens here
    optimizedParameters, pcov = opt.curve_fit(func, xdata, ydata);

    # Use the optimized parameters to plot the best fit
    plt.plot(xdata, func(xdata, *optimizedParameters), label="fit");

    # Show the graph
    plt.legend();
    plt.show();

if __name__ == '__main__':

    Execute()


