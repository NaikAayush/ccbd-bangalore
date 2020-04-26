# pylint: disable=no-member

import os
import multiprocessing
import csv
import cv2
import numpy as np

## Read
input_folder_path = "../../Images_Vertical_1024px/23428"
save_green_images = False
output_folder_path = "../../Images_Vertical_1024px_green_23428"
os.makedirs(output_folder_path, exist_ok=True)
size = 1024*1024
output_csv_prefix = "output_{}.csv"
concatenated_csv = "output.csv"
number_of_threads = 8

def greener(image_filenames, output_csv):
    with open(output_csv, "wt+") as csvfile:
        # image_filenames = os.listdir(input_folder_path)
        # print("original images list:", image_filenames)
        # csvfile.seek(0)
        # csvreader = csv.reader(csvfile, delimiter=",")
        # skipped_count = 0
        # for row in csvreader:
            # img_file, green = row
            # image_filenames.remove(img_file)
            # skipped_count += 1
        # print("Skipped {} images already in CSV".format(skipped_count))
        # print("final images list:", image_filenames)
        csvwriter = csv.writer(csvfile, delimiter=",")
        for img_file in image_filenames:
            img = cv2.imread(os.path.join(input_folder_path, img_file))
            name = str(img_file)
            print("Processing File:", name, "in process", multiprocessing.current_process().name)
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
            # print('GREEN: ' + str(percent_GREEN) + '%')
            csvwriter.writerow([img_file, percent_GREEN])

            ###############

            ## save
            if save_green_images:
                cv2.imwrite(os.path.join(output_folder_path, img_file), green)

def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(n):
        yield l[i::n]

if __name__ == "__main__":
    jobs = []
    output_csv_filenames = [output_csv_prefix.format(i) for i in range(number_of_threads)]
    image_filenames = os.listdir(input_folder_path)

    # skip already processed images
    csvfile = open(concatenated_csv, "at+")
    csvfile.seek(0)
    csvreader = csv.reader(csvfile, delimiter=",")
    skipped_count = 0
    for row in csvreader:
        img_file, green = row
        image_filenames.remove(img_file)
        skipped_count += 1
    print("Skipped {} images already in CSV".format(skipped_count))

    image_filenames_chunks = list(chunks(image_filenames, number_of_threads))
    for i, filenames_chunk, output_csv in zip(range(number_of_threads), image_filenames_chunks, output_csv_filenames):
        p = multiprocessing.Process(target=greener, args=(filenames_chunk, output_csv))
        p.start()
        jobs.append(p)
    for job in jobs:
        job.join()
    print("Done processing. Now concatenating all CSVs into one.")

    for output_csv in output_csv_filenames:
        with open(output_csv, "rt") as output_csv_f:
            for line in output_csv_f:
                csvfile.write(line)
    print("Done concatenating")
