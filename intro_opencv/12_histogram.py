import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


'''The histogram of an image shows the frequency of the intensity values.'''

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)


# Create a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#  create a circle mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


# create a mask
masked =  cv.bitwise_and(img, img, mask=mask)  
cv.imshow('Mask', masked)

''' 
----Grayscale histogram---
 256 is the number of bins, 
 and [0,256] 
 is the range of the values
''' 
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])


# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
#  plt.xlim([0,256])
# plt.show()

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

# Color histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()


cv.waitKey(0)