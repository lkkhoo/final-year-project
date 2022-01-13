import cv2

img1 = cv2.imread("potato1.jpg")
img2 = cv2.imread("puppygrey1.jpg")
psnr = cv2.PSNR(img1, img2)
print(psnr)