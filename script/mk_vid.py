import cv2
import numpy as np
import glob

INPUT_FULLPATH = "/Users/mark/Documents/CODE/rpi-projects/script/vid1/*.jpg"
OUTPUT_FILE_NAME = "project.avi"
OUTPUT_FPS = 24
IMAGE_SHAPE = (1024, 768)

img_array = []
for filename in sorted(glob.glob(INPUT_FULLPATH)):
    img = cv2.imread(filename)
    img_array.append(img)

out = cv2.VideoWriter(OUTPUT_FILE_NAME, cv2.VideoWriter_fourcc(*'DIVX'), OUTPUT_FPS, IMAGE_SHAPE)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()
