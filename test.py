# 灰度图像的高斯滤波
from scanLine4e import scanLine4e
from rgb1gray import rgb1gray
from twodConv import twodConv
from gaussKernel import gaussKernel
import cv2
import numpy as np
from matplotlib import pyplot as plt

w_sig1 = gaussKernel(1)
w_sig2 = gaussKernel(2)
w_sig3 = gaussKernel(3)
w_sig5 = gaussKernel(5)

img1 = twodConv('cameraman.tif', w_sig1, 'replicate')
img2 = twodConv('einstein.tif', w_sig2, 'replicate')
img3 = twodConv('lena_gray.tiff', w_sig3, 'replicate')
img5 = twodConv('mandril_gray.tif', w_sig5, 'replicate')
img3_zero = twodConv('lena_gray.tiff', w_sig3, 'zero')
img5_zero = twodConv('mandril_gray.tif', w_sig3, 'zero')

raw = cv2.GaussianBlur(cv2.imread('cameraman.tif', 0), (7, 7), 1)

difference = cv2.absdiff(img1, raw)
difference1 = cv2.absdiff(img3, img3_zero)
difference2 = cv2.absdiff(img5, img5_zero)
print(difference1[0])
# print(np.max(img1), np.max(raw))
cv2.imshow('deference', difference)
cv2.imshow('difference1', difference1)
cv2.imshow('difference2', difference2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img5', img5)
cv2.imshow('raw', raw)

# cv2.imwrite('img1.tif', img1)
# cv2.imwrite('img2.tif', img2)
# cv2.imwrite('img3.tif', img3)
# cv2.imwrite('img5.tif', img5)
# cv2.imwrite('raw.tif', raw)
# cv2.imwrite('difference.tif', difference)


cv2.waitKey(0)
