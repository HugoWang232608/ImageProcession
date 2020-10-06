# 彩色图像转换为黑白图像
import numpy as np
import cv2
from matplotlib import pyplot as plt


def rgb1gray(f, method='NTSC'):
    """
    Convert color images to gray in two ways
    :param f: the path and the filename of the image
    :param method: convert method, default method is 'NTSC'
    :return: return the gray image
    """
    img = cv2.imread(f, 1)
    img_size = img.shape
    height = img_size[0]
    width = img_size[1]  # get the size of the image
    res = np.zeros((height, width, 3), dtype=np.uint8)  # set the format of the result
    for i in range(0, height):
        for j in range(0, width):
            (b, g, r) = img[i][j]  # get the RGB of each pixel
            if method == 'average':
                res[i][j] = np.uint8((int(b) + int(g) + int(r)) / 3)  # the method of 'average'
            elif method == 'NTSC':
                res[i][j] = np.uint8(int(r) * 0.2989 + int(g) * 0.5870 + int(b) * 0.1140)  # the method of 'NTSC'
            else:
                print("Error: wrong method, the method must be 'average' or 'NTSC'")
    return res


if __name__ == '__main__':
    filename1 = 'lena512color.tiff'
    filename2 = 'mandril_color.tif'
    img1 = rgb1gray(filename1, 'average')
    img2 = rgb1gray(filename1)
    img3 = rgb1gray(filename2, 'average')
    img4 = rgb1gray(filename2)
    imgs1 = np.hstack([img1, img2])  # put the same images in the same window
    imgs2 = np.hstack([img3, img4])
    cv2.imshow('imgs1', imgs1)
    cv2.imshow('imgs2', imgs2)
    # cv2.imwrite('lena_gray.tiff', img2)
    # cv2.imwrite('mandril_gray.tif', img4)
    cv2.waitKey(0)
