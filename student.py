import math
import random
import matplotlib.pyplot as plt

x1, y1 = 0, 0
x2, y2 = 0, 0

x1_coords = []
y1_coords = []

x2_coords = []
y2_coords = []

# take same length steps until 200 is reached
for step in range(200):

    # Student 1: sample coordinates with random angles and 
    # add them to the list of coordinates
    angle1 = random.uniform(0, 2 * math.pi)
    x1 += math.cos(angle1)
    y1 += math.sin(angle1)
    x1_coords.append(x1)
    y1_coords.append(y1)

    # Student 2: sample coordinates with random angles and 
    # add them to the list of coordinates
    angle2 = random.uniform(0, 2 * math.pi)
    x2 += math.cos(angle2)
    y2 += math.sin(angle2)
    x2_coords.append(x2)
    y2_coords.append(y2)

    # clear graph of previous points
    plt.clf()

    # plot graph
    plt.plot(x1_coords, y1_coords, 'b-')     # blue line
    plt.plot(x2_coords, y2_coords, 'g-')     # green line
    plt.plot(x1, y1, 'bo', markersize = 10)  # blue dot
    plt.plot(x2, y2, 'go', markersize = 10)  # green dot
    plt.plot([x1, x2], [y1, y2], 'b-')     # blue line between students
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)

    # text on the screen      
    plt.text(-15, -15, f"step {step}/200" )  

    # update graph
    plt.draw()         
    plt.pause(0.1)

plt.show()