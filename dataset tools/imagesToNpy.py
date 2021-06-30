import os
import sys
import cv2
import numpy as np

def main():
	data = sys.argv[1:]
	src_path = data[0]
	dst_file = data[1]
	arr = []
	for path, subdirs, files in os.walk(src_path):
		for name in files:
			full_input_path = os.path.join(path, name)
			img = cv2.imread(full_input_path)
			img = cv2.resize(img, (256,256))
			arr.append(img)
	x = np.array(arr)
	print(x.shape)
	print(x.shape[0])
	np.save(dst_file,x)

if __name__ == '__main__':
    main()