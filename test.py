import cv2
import numpy as np

image = np.zeros([960, 960, 3])

image[:, :, ]=np.array([96, 52, 23])

cv2.imshow('xx', image)
cv2.waitKey(0)