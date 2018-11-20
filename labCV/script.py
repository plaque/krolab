#!/usr/bin/python3

import numpy as np
import cv2
import matplotlib.pyplot as plt

def create_blob_detector(roi_size=(128, 128), blob_min_area=3, 
                         blob_min_int=.5, blob_max_int=.95, blob_th_step=10):
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = blob_min_area
    params.maxArea = roi_size[0]*roi_size[1]
    params.filterByCircularity = False
    params.filterByColor = False
    params.filterByConvexity = False
    params.filterByInertia = False
    # blob detection only works with "uint8" images.
    params.minThreshold = int(blob_min_int*255)
    params.maxThreshold = int(blob_max_int*255)
    params.thresholdStep = blob_th_step
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3:
        return cv2.SimpleBlobDetector(params)
    else:
        return cv2.SimpleBlobDetector_create(params) 


detector = create_blob_detector()


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 400, 300)
cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image1', 400, 300)

# Wczytaj obrazek z pliku z różnymi opcjami
img = cv2.imread('water_coins.jpg')

kernel = np.zeros((10,10),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 10)
dilation = cv2.dilate(img,kernel,iterations = 10)
keypoints = detector.detect(dilation)
keypoints1 = detector.detect(erosion)
print(len(keypoints))
print(len(keypoints1))

im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
im_with_keypoints = cv2.drawKeypoints(img, keypoints1, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('image',dilation)
cv2.imshow('image1',erosion)
cv2.waitKey(0)

# Zapisz plik docelowy na dysku
# cv.imsave()

cv2.destroyAllWindows()
