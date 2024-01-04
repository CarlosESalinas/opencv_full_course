import cv2 as cv


img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

## Average Blur
average = cv.blur(img, (5,5))
cv.imshow('Average Blur', average)

#  Gaussian Blur
gauss = cv.GaussianBlur(img, (5,5), 0)
# We need to specify the standard deviation in the x and y directions, we can leave it as 0
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median) 


# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
# 10 --> diameter of the pixel neighborhood
# 35 --> sigma color, how much the colors are mixed together
# 25 --> sigma space, how far the pixels are mixed together
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)