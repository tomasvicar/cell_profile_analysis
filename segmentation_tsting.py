import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion, binary_dilation,erosion, dilation, label, disk
import utils
from skimage.segmentation import random_walker, watershed
from visboundaries import visboundaries
from skimage import filters

img = np.max(imread(r"C:\Users\vicar\Desktop\cell_profile_analysis\cell_profile_analysis\example_data\63x_B3_F-actin+TAG_1_4.tif"), axis=0)
mask = imread(r"C:\Users\vicar\Desktop\cell_profile_analysis\cell_profile_analysis\example_data\xxx.png")


label_img = utils.toUniqueLabel(mask)
N = np.max(label_img)


se = disk(20)

original_bg = label_img == 0
for cell_num in range(1, N+1):
    bin_cell = label_img == cell_num
    label_img[bin_cell] = 0
    
    bin_cell = binary_erosion(bin_cell, se)
    label_img[bin_cell] = cell_num
    
   

original_bg = binary_erosion(original_bg, se)
label_img[original_bg] = N + 1 


plt.imshow(label_img)
plt.show()

img = img[0,:,:]

Gx = filters.sobel_h(img)
Gy = filters.sobel_v(img)
magnitude = np.sqrt(Gx ** 2 + Gy ** 2)

segmentation = watershed(magnitude, label_img)
# segmentation = random_walker(magnitude, label_img, beta=10)

segmentation[segmentation == N +1] = 0
plt.imshow(segmentation)
plt.show()

plt.figure(figsize=(20, 20))
plt.imshow(img)
for cell_num in range(1, N+1):
    bin_cell = segmentation == cell_num
    visboundaries(bin_cell)
    
    
plt.show()


