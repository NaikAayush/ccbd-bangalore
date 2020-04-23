from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
%matplotlib inline

abs_path = "/home/etherealenvy/github/ccbd-bangalore/GreenDetection/Images_Vertical_1024px/23428/15175.jpg"
img = cv2.imread(abs_path)
name = abs_path.split("/")[-2]+"/"+abs_path.split("/")[-1]


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_colors(image, number_of_colors, show_chart):
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)

    center_colors = clf.cluster_centers_

    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)

    return rgb_colors
    
get_colors(get_image(abs_path), 8, True)



# #We’ll now dive into the code of filtering a set of five images based on the color we’d like
# IMAGE_DIRECTORY = 'images'
# COLORS = {
#     'GREEN': [0, 128, 0],
#     'BLUE': [0, 0, 128],
#     'YELLOW': [255, 255, 0]
# }
# images = []

# for file in os.listdir(IMAGE_DIRECTORY):
#     if not file.startswith('.'):
#         images.append(get_image(os.path.join(IMAGE_DIRECTORY, file)))

# #show all images we will be using
# # plt.figure(figsize=(20, 10))
# # for i in range(len(images)):
# #     plt.subplot(1, len(images), i+1)
# #     plt.imshow(images[i])

# # to filter all images that match the selected color.
# def match_image_by_color(image, color, threshold = 60, number_of_colors = 10): 
    
#     image_colors = get_colors(image, number_of_colors, False)
#     selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

#     select_image = False
#     for i in range(number_of_colors):
#         curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
#         diff = deltaE_cie76(selected_color, curr_color)
#         if (diff < threshold):
#             select_image = True
    
#     return select_image

# def show_selected_images(images, color, threshold, colors_to_match):
#     index = 1
    
#     for i in range(len(images)):
#         selected = match_image_by_color(images[i],
#                                         color,
#                                         threshold,
#                                         colors_to_match)
#         if (selected):
#             plt.subplot(1, 5, index)
#             plt.imshow(images[i])
#             index += 1
#     return True

# # Variable 'selected_color' can be any of COLORS['GREEN'], COLORS['BLUE'] or COLORS['YELLOW']
# plt.figure(figsize = (20, 10))
# show_selected_images(images, selected_color, 60, 5)