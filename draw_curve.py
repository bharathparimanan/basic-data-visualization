# Here is an example plot showing a sinusoid.
# For the next exercise, you can use bits
# of this code for your own program.

import matplotlib.pyplot as plt
import numpy as np

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.grid(color='lightgray')

ax.plot(x, y, linewidth=2.0, color='black')

# Set plot range and tic parameters
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

ax.tick_params(labelsize=14) # increase label font size

# Labels the axes
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

plt.show() # With jupyter notebooks there is no need to include this line
