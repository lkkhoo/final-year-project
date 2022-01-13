import cv2
import numpy as np
import math

tmp = []
for i in range(256):
    tmp.append(0)
val = 0
k = 0
res = 0

image = cv2.imread('puppygrey1_enc.jpg',0)
img = np.array(image)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        val = img[i][j]
        tmp[val] = float(tmp[val] + 1)
        k =  float(k + 1)
for i in range(len(tmp)):
    tmp[i] = float(tmp[i] / k)
for i in range(len(tmp)):
    if(tmp[i] == 0):
        res = res
    else:
        res = float(res - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))
print(res)
