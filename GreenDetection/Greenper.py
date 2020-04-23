import cv2
import numpy as np

img = cv2.imread('roi.jpg')
size = img.size

#replace green threshold
GREEN_MIN = np.array([0,0,128], np.uint8)
GREEN_MAX = np.array([250, 250, 255], np.uint8)


dstr = cv2.inRange(img, GREEN_MIN, GREEN_MAX)
no_GREEN = cv2.countNonZero(dstr)

frac_GREEN = np.divide((float(no_GREEN)),(float(size)))
percent_red = np.multiply((float(frac_GREEN)), 100)
print('GREEN: ' + str(percent_GREEN) + '%')