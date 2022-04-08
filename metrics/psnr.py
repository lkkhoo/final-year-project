

import math
import os

import cv2
import numpy as np

def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR


def main():

    # Loading images (original image and compressed image)
    original = cv2.imread("cameraman.tif")
    contrast = cv2.imread("lfsr1.png", 1)

    print(f"PSNR value is {psnr(original, contrast)} dB")




if __name__ == '__main__':
    main()

