import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_img():
	img=np.ones((600,600))
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,text='ABCDE',org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
	return img


def show_img(img):
	fig=plt.figure(figsize=(15,15))
	ax=fig.add_subplot(111)
	ax.imshow(img,cmap='gray')
	plt.show()


i=load_img()


kernel=np.ones((5,5),dtype=np.uint8)

black_noise=np.random.randint(low=0,high=2,size=(600,600))

black_noise=black_noise *(-255)


black_noise_img= black_noise_img+i 
black_noise_img[black_noise_img ==-255]=0

show_img(black_noise_img)