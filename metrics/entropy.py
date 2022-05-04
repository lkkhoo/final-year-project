import skimage.measure
import cv2

im = cv2.imread('encrypted images/peppers_10rounds.png')

entropy = skimage.measure.shannon_entropy(im)

print(entropy)
