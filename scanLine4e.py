# 黑白图像灰度扫描
import cv2
import numpy as np
from matplotlib import pyplot as plt


def scanLine4e(f, I, loc):
    """

    :param f: the image filename
    :param I: It will be a row or a column of the image
    :param loc: 'row' or 'column' which determines the param I
    :return: a certain row or column of the image
    """
    img = cv2.imread(f, 0)
    if loc == 'row':
        res = img[I - 1, :]
    elif loc == 'column':
        res = img[:, I - 1]
    else:
        print("Error: loc must be 'row' or'colume'")
    return res


if __name__ == '__main__':
    img1 = cv2.imread('cameraman.tif', 0)
    img2 = cv2.imread('einstein.tif', 0)
    hw1 = img1.shape  # get the height and the width of the image
    hw2 = img2.shape
    plt.figure()
    plt.title('cameraman row')
    plt.plot(scanLine4e('cameraman.tif', int(hw1[0] / 2), 'row'))  # read the middle row of the image(cameraman.tif)
    plt.figure()
    plt.title('cameraman column')
    plt.plot(scanLine4e('cameraman.tif', int(hw1[1] / 2), 'column'))
    plt.figure()
    plt.title('einstein row')
    plt.plot(scanLine4e('einstein.tif', int(hw2[0] / 2), 'row'))
    plt.figure()
    plt.title('einstein column')
    plt.plot(scanLine4e('einstein.tif', int(hw2[1] / 2), 'column'))
    plt.show()
    # cv2.imwrite('result.tif', scanLine4e('cameraman.tif', int(hw1[0]/2), 'row'))
