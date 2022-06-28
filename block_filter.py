import cv2
import numpy as np
from math import ceil
from PIL import Image
from check_img import check_img
from get_patch import get_patch
from get_patch_single import get_patch_single
from similarity import similarity
from SNR import SNR


img1 = cv2.imread('images/phantom_noisy.png')
# img1 = cv2.imread('images/1.png')
img1 = np.pad(img1, ((6, 6), (0, 0), (0, 0)), 'edge')
h, w = img1.shape[0], img1.shape[1]
scale = 0.5
# img1 = cv2.resize(img1, dsize=(int(scale*h+1), int(scale*w+1)), interpolation=cv2.INTER_CUBIC)
img1 = np.array(Image.fromarray(img1).resize((ceil(scale*w), ceil(scale*h)), Image.BICUBIC))
img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)

search_window = 6  # search window for NL means
patch_size = 3     # patch size for comparison
epsilon = 1e-13   # to handle 0/0 cases

g_mean = np.mean(img1)  # mean
g_var = np.var(img1)    # variance

filtered_img = np.ones((img1.shape[0], img1.shape[1]))

for i in range(1, img1.shape[0] + 1):
    for j in range(1, img1.shape[1] + 1):
        if check_img(img1, i, j, search_window, patch_size) == 1:
            patch1, patch2, patch3, patch4 = get_patch(img1, i, j, patch_size)

            # Mean and Variance of patches
            mean_patch1 = np.mean(patch1) + epsilon
            var_patch1 = np.var(patch1) + epsilon

            mean_patch2 = np.mean(patch2) + epsilon
            var_patch2 = np.var(patch2) + epsilon

            mean_patch3 = np.mean(patch3) + epsilon
            var_patch3 = np.var(patch3) + epsilon

            mean_patch4 = np.mean(patch4) + epsilon
            var_patch4 = np.var(patch4) + epsilon

            count = 0
            v1 = []
            v2 = []
            v3 = []
            v4 = []
            loc1 = []
            loc2 = []
            loc3 = []
            loc4 = []
            # Block wise comparisions with Pearson Distance
            for x in range(int(1 + i-(search_window-1) / 2), int(1 + i + (search_window - 1) / 2) + 1):
                for y in range(int(1 + j-(search_window-1) / 2), int(1 + j + (search_window - 1) / 2) + 1):
                    sub_patch = get_patch_single(img1, x, y, patch_size)
                    mean_sub_patch = np.mean(sub_patch) + epsilon
                    var_sub_patch = np.var(sub_patch) + epsilon
                    if (g_mean > mean_patch1 / mean_sub_patch > 1 / g_mean) and \
                        (g_var > var_patch1 / var_sub_patch > 1 / g_var):
                        count = count + 1
                        norm = similarity(patch1, sub_patch)
                        v1.append(norm)
                        loc1.append(img1[x-1, y-1])

                    if (g_mean > mean_patch2 / mean_sub_patch > 1 / g_mean) and \
                            (g_var > var_patch2 / var_sub_patch > 1 / g_var):
                        count = count + 1
                        norm = similarity(patch2, sub_patch)
                        v2.append(norm)
                        loc2.append(img1[x-1, y-1])

                    if (g_mean > mean_patch3 / mean_sub_patch > 1 / g_mean) and \
                        (g_var > var_patch3 / var_sub_patch > 1 / g_var):
                        count = count + 1
                        norm = similarity(patch3, sub_patch)
                        v3.append(norm)
                        loc3.append(img1[x-1, y-1])

                    if (g_mean > mean_patch4 / mean_sub_patch > 1 / g_mean) and \
                            (g_var > var_patch4 / var_sub_patch > 1 / g_var):
                        count = count + 1
                        norm = similarity(patch4, sub_patch)
                        v4.append(norm)
                        loc4.append(img1[x-1, y-1])

            v1 = np.array(v1)
            v2 = np.array(v2)
            v3 = np.array(v3)
            v4 = np.array(v4)
            loc1 = np.array(loc1)
            loc2 = np.array(loc2)
            loc3 = np.array(loc3)
            loc4 = np.array(loc4)

            v1_sum = np.sum(v1)
            v1 = (v1 + 1e-13) / (v1_sum + 1e-13)

            v2_sum = np.sum(v2)
            v2 = (v2 + 1e-13) / (v2_sum + 1e-13)

            v3_sum = np.sum(v3)
            v3 = (v3 + 1e-13) / (v3_sum + 1e-13)

            v4_sum = np.sum(v4)
            v4 = (v4 + 1e-13) / (v4_sum + 1e-13)

            pixel1 = np.vdot(v1, loc1)
            pixel2 = np.vdot(v2, loc2)
            pixel3 = np.vdot(v3, loc3)
            pixel4 = np.vdot(v4, loc4)

            filtered_img[i-1, j-1] = (pixel1 + pixel2 + pixel3 + pixel4) / 4

    print("Completed Pixel {} {}".format(i, j))

filtered_img = filtered_img.astype(np.uint8)
print("SNR: {}".format(SNR(filtered_img, img1)))
cv2.imshow("NL Means Speckle Filter", filtered_img)
cv2.waitKey(0)