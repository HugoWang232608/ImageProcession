#  图像二维卷积函数
import cv2
import numpy as np


def twodConv(f, w, padding='zero'):
    """
    2D convolution
    :param f: the path and filename of a image
    :param w: convolution kernel
    :param padding: the method to extend the matrix
    :return: the image after convolution
    """
    img = cv2.imread(f, 0)
    [height, width] = img.shape
    k = w.shape[0]
    r = int(k / 2)
    w_new = np.rot90(w, 2)  # convolution kernel rotate 180°
    if padding == 'replicate':
        img_padding = cv2.copyMakeBorder(img, r, r, r, r, cv2.BORDER_REPLICATE)  # extend the matrix
    elif padding == 'zero':
        img_padding = cv2.copyMakeBorder(img, r, r, r, r, cv2.BORDER_CONSTANT, value=0)
    else:
        img_padding = img  # make sure the img_padding is assigned a value
        print("Error: wrong input！")

    tmp = img_padding.copy()
    for i in range(height):
        for j in range(width):
            img_padding[i + r, j + r] = np.sum(w_new * tmp[i:i+k, j:j+k])
    img_padding = np.clip(img_padding, 0, 255)
    img_padding = img_padding[r:r+height, r:r+width].astype(np.uint8)
    return img_padding
    # for i in range(r + 1, height + r + 1):
    #     for j in range(r + 1, width + r + 1):
    #         roi = img_padding[i - r - 1:i + r, j - r - 1:j + r]  # get the ROI
    #         img_new[i][j] = np.sum(w_new * roi)  # convolution
    # img = img_new[r + 1:height + r + 1, r + 1:width + r + 1]


if __name__ == '__main__':
    kernel = np.array([[0.07511362, 0.12384141, 0.07511362],
                       [0.12384141, 0.20417996, 0.12384141],
                       [0.07511362, 0.12384141, 0.07511362]])
    res = twodConv('cameraman.tif', kernel, padding='zero')
    cv2.imshow('res', res)
    cv2.waitKey(0)
