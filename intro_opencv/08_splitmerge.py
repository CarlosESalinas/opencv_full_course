import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# print(f'Shape of the image: {img.shape} \n Shape of the blue channel: {b.shape} \n Shape of the green channel: {g.shape} \n Shape of the red channel: {r.shape}')


blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


# merged = cv.merge([b,g,r])
# cv.imshow('Merged Image', merged)

# print(f'Shape of the merged image: {merged.shape}') 


cv.waitKey(0)
