import cv2 as cv 
import numpy as np


blank = np.zeros((400, 400), dytpe='uint8')    

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circule = cv.circule(blank.copy(), (200,200), 200, 255, -1)    


cv.imshow('Rectangle', rectangle)
cv.imshow('Circule', circule)


# Bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circule)
cv.imshow('Bitwise AND', bitwise_and)



# Bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circule)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circule)
cv.imshow('Bitwise XOR', bitwise_xor)


# Bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Rectangule NOT",bitwise_not)



cv.waitKey(0)