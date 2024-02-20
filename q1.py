import numpy as np
from PIL import Image

img = Image.open('clock_tower.png')

img_arr = np.array(img)

img_arr = img_arr.astype('uint64')

print(img_arr)

print("----------------------------------")

# n = int(input("Enter the scale factor for binning: "))
# new_image = img_arr[::n, ::n]
new_image = (img_arr[::2, ::2] + img_arr[1::2, ::2] + img_arr[::2, 1::2] + img_arr[1::2, 1::2]) // 4
# new_image = (img_arr[::2, ::2] + img_arr[::2, 1::2]) // 2
# new_image = np.maximum(np.maximum(img_arr[::2, ::2], img_arr[1::2, ::2]),
#                        np.maximum(img_arr[::2, 1::2], img_arr[1::2, 1::2]))
# new_image = np.minimum(np.minimum(img_arr[::2, ::2], img_arr[1::2, ::2]), np.minimum(img_arr[::2, 1::2],
#                                                                                      img_arr[1::2, 1::2]))

print(new_image)
out_img = Image.fromarray(new_image.astype('uint8'))

out_img.save('output_image.png')

# after experimentation it is concluded that the maximum value of the 4 pixels is the best method for this case
