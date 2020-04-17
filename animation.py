import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

frame = [[[1,2,3]],[[4,5,6]], [[7,8,9]]]
ani = FuncAnimation(fig, update, interval = 2000, frames= frame,
                    init_func=init, blit=False)
plt.show()

