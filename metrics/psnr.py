import cv2
img1 = cv2.imread('test images/baboon.tif')
img2 = cv2.imread('encrypted images/baboon_10rounds.png')
psnr = cv2.PSNR(img1, img2)
print(psnr)
