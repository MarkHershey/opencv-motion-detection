import numpy as np
import cv2 as cv

# Load a color image in grayscale
img = cv.imread('meredith_derek.jpg',0)

# Even if the image path is wrong, it won't throw any error, but print img will give you None


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
