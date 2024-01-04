import cv2 as cv


img = cv.imread('Photos/Boston.jpg')

cv.imshow('Boston', img)

## Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

## Blur
# Elimitates noise
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

## Edge Cascade
# Detects the edges of the image
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)


## Dilating the image
# Makes the edges thicker
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

## Eroding
# Makes the edges thinner
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize 
resized = cv.resize(img, (500,500), interpolations = cv.INTER_AREA)
cv.imshow('Resized', resized)


## Cropping
# Cropping the image from 50 to 200 in the height and 200 to 400 in the width
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)