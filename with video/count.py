# import the modules
import os
from os import listdir

count = 0
folder_dir = "C:\\Users\\rosha\\OneDrive\\Documents\\ExtraS\\Clubs\\Optizen\\SLAM\\frames"
for images in os.listdir(folder_dir):

	if (images.endswith(".png") or images.endswith(".jpg")\
		or images.endswith(".jpeg")):
		count += 1

print(count)
