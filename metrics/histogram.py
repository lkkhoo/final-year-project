import numpy as np
import matplotlib.pyplot as plt
import cv2
import statistics

# read image
im = cv2.imread('encrypted images/peppers_lfsr.png')

# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()

# calculate histogram
counts, bins = np.histogram(vals, range(257))

# plot histogram centered on values 0..255
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])

m = statistics.mean(counts)
sd = statistics.stdev(counts)
ma = max(counts)
mi = min(counts)

print("mean = " , m)
print()
print("standard deviation = " , sd)
print()
print("max y = " ,ma)
print()
print("min y = ",mi)

plt.axhline(m, color='k', linestyle='dashed')

plt.axhline(m + sd, color='r', linestyle='dashed')
plt.axhline(m - sd, color='r', linestyle='dashed')

plt.xlabel("Intensity")
plt.ylabel("Pixel Count")
plt.show()


