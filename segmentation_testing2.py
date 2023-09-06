import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion, binary_dilation,erosion, dilation, label, disk
import utils
from skimage.segmentation import random_walker, watershed, quickshift, mark_boundaries, felzenszwalb, slic
from visboundaries import visboundaries
from skimage import filters

img = np.max(imread(r"C:\Users\vicar\Desktop\cell_profile_analysis\cell_profile_analysis\example_data\63x_B3_F-actin+TAG_1_4.tif"), axis=0)
mask = imread(r"C:\Users\vicar\Desktop\cell_profile_analysis\cell_profile_analysis\example_data\xxx.png")


label_img = utils.toUniqueLabel(mask)
N = np.max(label_img)

img = img[0,:,:].astype(np.float32) / 100


# segments = quickshift(img, kernel_size=3, max_dist=6, ratio=0.5, convert2lab=False)
segments = felzenszwalb(img, scale=250, sigma=3, min_size=300)

plt.figure(figsize=(20, 20))
plt.imshow(mark_boundaries(img, segments, color=(1, 0, 0)))
plt.show()

