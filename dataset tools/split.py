import 	numpy as np	

dest = "/not/"
x = np.load("not.npy", mmap_mode='r')

images = x.shape[0]

step = int(images*0.1)

cnt = 0
for j in range(0,images-step,step):
	dest_file = str(cnt)+".npy"
	data = x[j:j+step]
	np.save(dest_file,data)
	print(data.shape)
	cnt+=1