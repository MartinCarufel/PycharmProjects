import pandas as pd
import numpy
import matplotlib.pyplot as plt
from time import sleep
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):


    # Add x and y to lists
    # xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    try:
        data = xs[-1] +1
    except:
        data = 0
    finally:
        xs.append(data)

    number = numpy.random.randint(1, 100)
    ys.append(number)

    # Limit x and y lists to 20 items
    # xs = xs[-40:]
    # ys = ys[-40:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot

    tick_step = len(xs)/10
    # print(len(xs))
    try:
        plt.xticks(numpy.arange(0, xs[-1]+xs[-1]/10, step=xs[-1]/10), rotation=90, ha='center', fontsize='x-small')
        print(numpy.arange(0, xs[-1], step=xs[-1]/10))
    except ZeroDivisionError:
        pass

    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=200)
plt.show()

