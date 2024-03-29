import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


# # plt.imshow(img)
# # plt.show()


 ## BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# ## BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# # cv.imshow('HSV', hsv)

# ## BGR to L*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# # BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)


# plt.imshow(rgb)
# plt.title('RGB Image with Matplotlib')
# plt.show()

## GRAY to BRG
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('Gray --> BGR', gray_bgr)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

cv.waitKey(0)
