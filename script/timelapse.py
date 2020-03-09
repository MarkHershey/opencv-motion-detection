from time import sleep
from picamera import PiCamera
from datetime import datetime

def timestamp():
    now = str(datetime.now())
    ts = ""
    for i in now[:-7]:
        if i in (" ", "-", ":"):
            pass
        else:
            ts += i
    return ts


def main():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.rotation = -90
    # camera.start_preview()
    # Camera warm-up time
    while True:
        ts = timestamp()
        camera.capture(f'{ts}.jpg')
        sleep(2)


if __name__ == "__main__":
    main()
