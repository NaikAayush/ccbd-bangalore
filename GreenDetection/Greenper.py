# pylint: disable=no-member

import os
import csv
import cv2
import numpy as np

## Read
input_folder_path = "../../Images_Vertical_1024px"
save_green_images = True
output_folder_path = "../../Images_Vertical_1024px_green"
output_csv = "greens.csv"
with open(output_csv, "wt") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    for f in os.listdir(input_folder_path):
        os.makedirs(os.path.join(output_folder_path, f), exist_ok=True)
        if os.path.isdir(os.path.join(input_folder_path, f)):
            for img_file in os.listdir(os.path.join(input_folder_path, f)):

                img = cv2.imread(os.path.join(input_folder_path, f, img_file))
                name = str(f) + "/" + str(img_file)
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
                size = 1024*1024
                no_GREEN = cv2.countNonZero(mask)
                # print(no_GREEN)
                frac_GREEN = np.divide((float(no_GREEN)), (int(size)))
                percent_GREEN = np.multiply((float(frac_GREEN)), 100)
                print('GREEN: ' + str(percent_GREEN) + '%')
                csvwriter.writerow([f, img_file, percent_GREEN])

                ###############

                ## save
                if save_green_images:
                    cv2.imwrite(os.path.join(output_folder_path, f, img_file), green)

