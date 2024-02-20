import numpy as np
from PIL import Image

img = Image.open('clock_tower.png')

img_arr = np.array(img)

img_arr = img_arr.astype('uint8')

print(img_arr.shape)

# for i in range(img_arr.shape[0]-1):
#     for j in range(img_arr.shape[1]-1):
#         for k in range(3):
#             img_arr[i][j][k] = (img_arr[i][j][k] + img_arr[i][j + 1][k] + img_arr[i + 1][j][k] + img_arr[i + 1][j + 1][k]) // 4
# n = int(input("Enter the scale factor for binning: "))
# new_image = img_arr[::n, ::n]
# new_image = (img_arr[::2, ::2] + img_arr[1::2, ::2] + img_arr[::2, 1::2] + img_arr[1::2, 1::2]) // 4
new_image = np.maximum(np.maximum(img_arr[::2, ::2], img_arr[1::2, ::2]),
                       np.maximum(img_arr[::2, 1::2], img_arr[1::2, 1::2]))
# new_image = np.minimum(np.minimum(img_arr[::2, ::2], img_arr[1::2, ::2]), np.minimum(img_arr[::2, 1::2], img_arr[1::2, 1::2]))
out_img = Image.fromarray(new_image.astype('uint8'))

out_img.save('output_image.png')

# after experimentation it is concluded that the maximum value of the 4 pixels is the best method for this case
