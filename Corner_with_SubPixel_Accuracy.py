import numpy as np
import cv2 as cv

print('processo1')
filename = "images/inclinado_hard.jpeg"
img = cv.imread(filename)
while 1:


  print('processo2')
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  # find Harris corners

  print('processo3')
  gray = np.float32(gray)

  print('processo4')
  dst = cv.cornerHarris(gray, 2, 3, 0.04)
  dst = cv.dilate(dst, None)

  print('processo5')
  ret, dst = cv.threshold(dst, 0.01 * dst.max(), 255, 0)
  dst = np.uint8(dst)

  print('processo6')
  # find centroids
  ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

  print('processo7')
  # define the criteria to stop and refine the corners
  criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
  corners = cv.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

  print('processo8')
  # Now draw them
  res = np.hstack((centroids, corners))
  res = np.intp(res)
  img[res[:, 1], res[:, 0]] = [0, 0, 255]
  img[res[:, 3], res[:, 2]] = [0, 255, 0]
  print('processo9')

  cv.imwrite("subpixel5.png", img)
  cv.imshow('frame', img)
print('fim')