# 高斯滤波核函数
import cv2
import numpy as np
from math import pi, exp


def gaussKernel(sig, m=0):
    """

    :param sig: sigma, standard deviation of gauss distribution
    :param m: the size of the kernel
    :return: the m*m gauss kernel
    """
    r = int(3 * sig) * 2 + 1
    if m == 0:  # the default size of the kernel is r = int(3 * sig) * 2 + 1
        m = r
    elif 0 < m < r:
        print("Warning: the kernel is too small!")
    w = np.zeros([m, m], np.float32)
    for i in range(int((1-m)/2), int((m-1)/2)+1):
        for j in range(int((1 - m) / 2), int((m - 1) / 2)+1):
            w[i+int((m-1)/2)][j+int((m-1)/2)] = 1/(2*pi*(sig**2))*exp(-(i**2+j**2)/(2*sig**2))  # gauss distribution

    weight = np.sum(w)
    res = w/weight

    return res


if __name__ == '__main__':
    s = gaussKernel(1,3)
    print(s)
    print(np.sum(s))
