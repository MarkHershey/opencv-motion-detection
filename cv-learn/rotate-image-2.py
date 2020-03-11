import numpy as np
import cv2 as cv

"""
flip(m, 0) is equivalent to flipud(m).

flip(m, 1) is equivalent to fliplr(m).
"""

def rotateClockwise90(img: np.ndarray) -> np.ndarray:
    if type(img) != np.ndarray:
        raise "Require numpy.ndarray as input"
    rotated = np.flip(np.transpose(img), 1)
    return rotated

def rotateCounterClockwise90(img: np.ndarray) -> np.ndarray:
    if type(img) != np.ndarray:
        raise "Require numpy.ndarray as input"
    rotated = np.flip(np.transpose(img), 0)
    return rotated


# Load a color image in grayscale
img = cv.imread('meredith_derek.jpg',0)
print(np.shape(img))

rotated = rotateClockwise90(img)
print(np.shape(rotated))

# Even if the image path is wrong, it won't throw any error, but print img will give you None


cv.imshow('image',img)
cv.imshow('rotated',rotated)
cv.waitKey(0)
cv.destroyAllWindows()
