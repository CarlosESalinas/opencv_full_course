import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Create a image with the same shape as the original image 
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Detecting contours is a very useful technique in computer vision
# to detect the shape of an object

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur 

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Finding the contours
# RETR_LIST --> retrieves all the contours
# RETR_EXTERNAL --> retrieves the external contours
# RETR_TREE --> retrieves all the hierarchical contours
# RETR_CCOMP --> retrieves all the contours and organizes them into a two-level hierarchy
# CHAIN_APPROX_NONE --> stores all the contour points
# CHAIN_APPROX_SIMPLE --> stores only the end points of the contours
# CHAIN_APPROX_TC89_L1 --> applies Teh-Chin chain approximation algorithm
# CHAIN_APPROX_TC89_KCOS --> applies Teh-Chin chain approximation algorithm


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# 125 --> threshold value
# 255 --> max threshold value
# cv.THRESH_BINARY --> thresholding type

cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Draw the contours
cv.drawContours(blank, contours, -1,(0,0,255),1)
# -1 --> draw all the contours
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)