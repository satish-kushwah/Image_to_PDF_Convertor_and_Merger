#creating pdf 
from PIL import Image
import os
imagenamelist=os.listdir('input_images')
for i in range(len(imagenamelist)):
	image1 = Image.open('input_images/'+imagenamelist[i])
	im1 = image1.convert('RGB')
	im1.save('pdf_generated/'+imagenamelist[i].split('.')[0]+'.pdf')
input('conversion done successfully, press enter to close program')