import numpy as np
import cv2

file_loc = "landScape.npy"

arr = np.load(file_loc)
print(arr.dtype)
print(arr.shape)
for a in arr:
	cv2.imshow("a", a)
	cv2.waitKey(0)
cv2.destroyAllWindows()