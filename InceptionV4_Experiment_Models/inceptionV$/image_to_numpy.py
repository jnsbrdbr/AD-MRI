import os

from PIL import Image
import numpy as np
import cv2
import cv

#Directory containing images you wish to convert
input_dir = "/home/marcia/Desktop/InceptionV4_Sept022017/data_01/validation"

directories = os.listdir(input_dir)

index = 0
index2 = 0
out = 0
new_array = 0
new_index_array = 0
index_array = 0

for folder in directories:
	#Ignoring .DS_Store dir
	if folder == '.DS_Store':
		pass

	else:
		print folder

		folder2 = os.listdir(input_dir + '/' + folder)
		index += 1

		for image in folder2:
			if image == ".DS_Store":
				pass

			else:
				index2 += 1

				im = Image.open(input_dir+"/"+folder+"/"+image) #Opening image
				im = (np.array(im)) #Converting to numpy array
				#im = im[:, :, :, ::-1]  ## According to SO

				try:
					im = cv2.cvtColor(im, cv.CV_GRAY2RGB)
					r = im[:,:,0] #Slicing to get R data
					g = im[:,:,1] #Slicing to get G data
					b = im[:,:,2] #Slicing to get B data

					## According to SO
					#r = (im[:, :, :, 0] -= 103.939)
					#g = (im[:, :, :, 1] -= 116.779)
					#b = (im[:, :, :, 2] -= 123.68)
					
					if index2 != 1:
						new_array = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)
						out = np.append(out, new_array, 0) #Adding new image to array shape of (x, 3, 100, 100) where x is image number

					elif index2 == 1:
						out = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)

					if index == 1 and index2 == 1:
						index_array = np.array([[index]])

					else:
						new_index_array = np.array([[index]], np.int8)
						index_array = np.append(index_array, new_index_array, 0)

				except Exception as e:
					print e
					#print "Removing image" + image
					#os.remove(input_dir+"/"+folder+"/"+image)

		print index

np.save('X_valid_00.npy', out) #Saving train image arrays
np.save('Y_valid_00.npy', index_array) #Saving train labels


