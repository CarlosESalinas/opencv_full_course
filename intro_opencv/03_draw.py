import cv2 as cv
import numpy as np


# # blank is a black image
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# # 1. Paint the image a certain color
# # blank[:] = 0, 255, 0
# # cv.imshow('Green', blank)
# #  1.1 Paint a certain part of the image a certain color
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red Square', blank)


# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# thickness = -1 fills the rectangle or cv.FILLED
cv.imshow('Rectangle', blank)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)


# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
    # thickness = -1 fills the circle or cv.FILLED
    # 40 is the radius
    #  (0,255,0) represents the color
    # (blank.shape[1]//2, blank.shape[0]//2) is the center of the circle
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thinckness=2)
cv.imsho('Line', blank)


# 5. Write text
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
    # cv.FONT_HERSHEY_TRIPLEX is the font
    # 1.0 is the scale
    # (0, 255, 0) is the color
    # thickness = 2

cv.imshow('Text', blank)
cv.waitKey(0)