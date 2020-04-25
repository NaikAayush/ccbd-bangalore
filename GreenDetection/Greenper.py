# pylint: disable=no-member

import os
import csv
import cv2
import numpy as np

## Read
input_folder_path = "../../Images_Vertical_1024px/23428"
save_green_images = False
output_folder_path = "../../Images_Vertical_1024px_green_23428"
os.makedirs(output_folder_path, exist_ok=True)
output_csv = "greens.csv"
size = 1024*1024
with open(output_csv, "wt") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    for img_file in os.listdir(input_folder_path):
        img = cv2.imread(os.path.join(input_folder_path, img_file))
        name = str(img_file)
        print("Processing File:", name)
        ## convert to hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        ## mask of green (36,25,25) ~ (86, 255,255)
        # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
        mask = cv2.inRange(hsv, (20, 25, 25), (160, 255, 255))

        ## slice the green
        imask = mask > 0
        green = np.zeros_like(img, np.uint8)
        green[imask] = img[imask]


        #######pixel counter code
        no_GREEN = cv2.countNonZero(mask)
        # print(no_GREEN)
        frac_GREEN = float(no_GREEN) / size # np.divide((float(no_GREEN)), (int(size)))
        percent_GREEN = frac_GREEN * 100 # np.multiply((float(frac_GREEN)), 100)
        print('GREEN: ' + str(percent_GREEN) + '%')
        csvwriter.writerow([img_file, percent_GREEN])

        ###############

        ## save
        if save_green_images:
            cv2.imwrite(os.path.join(output_folder_path, img_file), green)

