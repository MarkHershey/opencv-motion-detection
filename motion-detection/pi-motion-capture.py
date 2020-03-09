from datetime import datetime
import numpy as np
import cv2 as cv

# Standard Deviation Threshold
sdThresh = 10
# Display font
font = cv.FONT_HERSHEY_SIMPLEX


def timestamp():
    now = str(datetime.now())
    ts = ""
    for i in now[:-7]:
        if i in (" ", "-", ":"):
            pass
        else:
            ts += i
    return now, ts


def distMap(frame1, frame2):
    """outputs pythagorean distance between two frames"""
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)
    diff32 = frame1_32 - frame2_32
    norm32 = np.sqrt(
        diff32[:, :, 0] ** 2 + diff32[:, :, 1] ** 2 + diff32[:, :, 2] ** 2
    ) / np.sqrt(255 ** 2 + 255 ** 2 + 255 ** 2)
    dist = np.uint8(norm32 * 255)
    return dist


# cv.namedWindow("frame")
# cv.namedWindow("dist")

# create a VideoCapture object
# argument can be either the device index or the path of a video file.
cap = cv.VideoCapture(0)

ret, frame = cap.read()
frame = np.rot90(frame)

"""
cv.VideoCapture.get(propId)
cv.VideoCapture.set(propId, value)

3 CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
4 CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
5 CV_CAP_PROP_FPS Frame rate.
6 CV_CAP_PROP_FOURCC 4-character code of codec.
7 CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
"""
print(f"FRAME_WIDTH: {cap.get(3)}")
print(f"FRAME_HEIGHT: {cap.get(4)}")
print(f"FRAME_RATE: {cap.get(5)}")
cap.set(5, 12)
print(f"FRAME_RATE: {cap.get(5)}")

while ret:

    _, nextFrame = cap.read()
    nextFrame = np.rot90(nextFrame)

    # print("frame1:\n", frame1)
    # print("frame2:\n", frame2)
    # print("frame3:\n", frame3)
    # break

    # height=rows, width=cols, _ = 3 (BGR)
    rows, cols, _ = np.shape(frame)

    dist = distMap(frame, nextFrame)

    # apply Gaussian smoothing
    mod = cv.GaussianBlur(dist, (9, 9), 0)

    # apply thresholding
    _, thresh = cv.threshold(mod, 100, 255, 0)

    # calculate st dev test
    _, stDev = cv.meanStdDev(mod)

    # show Standard Deviation on the frame
    # cv.putText(frame2, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv.LINE_AA)

    if stDev > sdThresh:
        now, ts = timestamp()
        print(f" --- {now}: Movement Detected | stDev: {stDev}")
        cv.imwrite(f"{ts}.jpg", frame)

    # show frames
    # cv.imshow("dist", mod)
    # cv.imshow("frame", frame)

    # shift frame
    frame = nextFrame

    # press "Q" on keyboard to quit
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
