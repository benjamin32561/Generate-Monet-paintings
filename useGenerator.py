import os
import sys
import cv2
import numpy as np
import tensorflow as tf

#python useGenerator.py model_path img_path
def main():
	save_at = "results_images/"
	img_name = str(len(os.listdir(save_at))+1)+".jpg"
	data = sys.argv[1:]
	model_path = data[0]
	img_path = data[1]
	img = cv2.imread(img_path)
	img = cv2.resize(img, (256,256))
	model = tf.keras.models.load_model(model_path)

	generated_img = np.array(model.predict(np.array([img/255.0]))[0]*255,dtype=np.uint8)

	imgs = cv2.hconcat([img, generated_img])
	cv2.imshow("images", imgs)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imwrite(save_at+img_name, imgs)

if __name__ == '__main__':
    main()