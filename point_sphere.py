# A line of dots is drawn along the prime meridian (longitude = 0 degrees)
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(projection="aitoff")
plt.title("Aitoff")
plt.grid(True)

lats = np.array(np.linspace(-90,90,13)) * np.pi / 180
lons = np.array(np.zeros(13)) * np.pi / 180

plt.plot(lons, lats, 'o', markersize=6, color='blue')

plt.xlabel('Lon.')
plt.ylabel('Lat.')
plt.show()