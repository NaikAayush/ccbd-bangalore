# import cv2
# import numpy as np

# img = cv2.imread('/home/etherealenvy/github/ccbd-bangalore/GreenDetection/Images_Vertical_1024px/23428/15175.jpg')
# size = img.size

# #replace green threshold in BGR form cause openCV reads numpy arrays in reverse order
# GREEN_MIN = np.array([0,0,0], np.uint8)
# GREEN_MAX = np.array([250, 255, 255], np.uint8)


# dstr = cv2.inRange(img, GREEN_MIN, GREEN_MAX)
# no_GREEN = cv2.countNonZero(dstr)

# frac_GREEN = np.divide((float(no_GREEN)),(float(size)))
# percent_GREEN = np.multiply((float(frac_GREEN)), 100)
# print('GREEN: ' + str(percent_GREEN) + '%')

import cv2
import numpy as np

## Read
abs_path = "/home/etherealenvy/github/ccbd-bangalore/GreenDetection/Images_Vertical_1024px/23428/15175.jpg"
img = cv2.imread(abs_path)
name = abs_path.split("/")[-2]+"/"+abs_path.split("/")[-1]
# print(name)
## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask = cv2.inRange(hsv, (35, 25, 25), (160, 255,255))

## slice the green
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## save 
cv2.imwrite(name, green)