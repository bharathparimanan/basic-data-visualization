import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate 500 uniformly distributed between 0 and 10 in x and y
x = np.random.uniform(0, 10, 500)
y = np.random.uniform(0, 10, 500)

fig, ax = plt.subplots()

# Do you recall what all of this is doing?
# If not, experiment with the parameters to
# test how it works.
ax.scatter(x, y, color='#0000FF', marker='o', s=10)
ax.tick_params(axis='both', labelsize=14)
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.show()