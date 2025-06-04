import math
import numpy as np
import matplotlib.pyplot as plt

def arange(start, stop, step):
    my_list = []

    while start < stop:
        my_list.append(start)
        start += step

    return my_list

# vary angle alpha between 0 to 20 radians in steps of 0.1
for angle in arange(0, 20, 0.1):
    # calculate radius based on alpha
    r = 10 - 0.5 * angle

    # convert to Cartesian coordinates
    x = r * math.cos(angle)
    y = r * math.sin(angle)

    # plot graph
    plt.plot(x, y, 'bo', markersize = 10)  # blue point
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_aspect('equal')  # keep square aspect ratio 

    # update graph
    plt.draw()
    plt.pause(0.05)