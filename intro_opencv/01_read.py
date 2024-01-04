import cv2 as cv

'''
# REDING IMAGES
img = cv.imread('Photos/cat.jpg')

# show image
cv.imshow('Cat', img)

# wait for a key to be pressed
cv.waitKey(0)
'''


## READ VIDEOS

# the  number is the index of the camera
# capture = cv.VideoCapture(0)

# read a video file
capture = cv.VideoCapture('Videos/dog.mp4')

# read the video frame by frame 
while True:
    isTrue, frame = capture.read()
    # show the frame
    cv.imshow('Video', frame)

    # if the d key is pressed, break the loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release the capture
capture.release()
# destroy all windows
cv.destroyAllWindows()

