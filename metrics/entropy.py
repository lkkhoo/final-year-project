import skimage.measure
import cv2

im = cv2.imread('lfsr1.png')

entropy = skimage.measure.shannon_entropy(im)

print(entropy)
