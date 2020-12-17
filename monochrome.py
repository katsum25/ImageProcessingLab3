import numpy as np


def monochrome(img):
    height, width, _ = img.shape
    res = np.zeros(shape=(height, width), dtype='uint8')

    for x in range(width):
        for y in range(height):
            B = img[y, x, 0]
            G = img[y, x, 1]
            R = img[y, x, 2]

            s = 0.2952 * R + 0.5547 * G + 0.148 * B
            res[y, x] = s

    return res