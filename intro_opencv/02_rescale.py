import cv2 as cv 

# RESIZING AND RESCALING FRAMES

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)


# Function to rescale the image
def rescaleFrame(frame, scale=0.75):
    # images, videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    # interpolation is the algorithm used to resize the image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#  RESIZING IMAGES
# resized_image = rescaleFrame(img)
# cv.imshow('Image Resized', resized_image)   


# Change the resolution of a video/image
# Function to change the resolution of the video
def changeRes(width, height):
    # only for live video
    capture.set(3, width)
    capture.set(4, height)

## Reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

# While loop to read the video frame by frame
while True:
    isTrue, frame = capture.read()

    # Rescale the frame
    frame_resized = rescaleFrame(frame, scale=.3)
    # Show the frame
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture
cv.destroyAllWindows()