import math
import matplotlib.pyplot as plt

def arange(start, stop, step):
    my_list = []

    while start < stop:
        my_list.append(start)
        start += step

    return my_list

x_coords = []
y_coords = []

# take small steps in x
for x in arange(0, 2 * math.pi, 0.05):

    y = math.sin(x)

    x_coords.append(x)
    y_coords.append(y)

    # plot graph
    plt.plot(x_coords, y_coords, 'r-')   # red line
    plt.xlim(0,2 * math.pi)
    plt.ylim(-1, 1)

    # update graph
    plt.draw()           
    plt.pause(0.001)
    plt.show()  

    # clear graph
    plt.clf()     