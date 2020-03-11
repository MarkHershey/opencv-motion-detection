"""
https://note.nkmk.me/en/python-opencv-numpy-rotate-flip/
"""


import numpy as np
import cv2 as cv


# Load a color image in grayscale
img = cv.imread('meredith_derek.jpg',0)


print(np.shape(img))
"""
When the second argument is omitted,
the default rotation is 90 degrees counterclockwise,
and when the second argument is 2 and 3,
the rotation is 180 degrees and 270 degrees counterclockwise.
"""
img = np.rot90(img)
print(np.shape(img))

# Even if the image path is wrong, it won't throw any error, but print img will give you None


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
