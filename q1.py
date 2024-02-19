import numpy as np
from PIL import Image

img = Image.open('clock_tower.png')


img_arr = np.array(img)

img_arr = img_arr.astype('uint8')


# for i in range(img_arr.shape[0]-1):
#     for j in range(img_arr.shape[1]-1):
#         img_arr[i][j] = (img_arr[i][j] + img_arr[i][j + 1] + img_arr[i + 1][j] + img_arr[i + 1][j + 1]) // 4
n = int(input("Enter the scale factor for binning: "))
new_image = img_arr[::n, ::n]

out_img = Image.fromarray(new_image.astype('uint8'))


out_img.save('output_image.png')
