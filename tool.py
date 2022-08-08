#code inspiration from https://stackoverflow.com/questions/59270464/python-navigate-through-and-show-images-in-a-folder

import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
import shutil


input_images_path = ".\\source\\"  #source image path, assuming program is in same folder
output_images_path1 = ".\\target1\\" #multiple targets, more can be added
output_images_path2 = ".\\target2\\"

#Array to loop through each image in source folder
images_list = [image_name for image_name in os.listdir(input_images_path)]

print("Press left for previous image, right for next one, 'c' to copy image to target 1 't' to copy image to target 2 and corresponding label." )

index = 0
while(True):
        img = cv2.imread(input_images_path+images_list[index], 1) #set img variable as first image in folder
        cv2.imshow(f'current image', img) #display current image
        key = cv2.waitKeyEx(0) #get user input
        
        if key == ord('c'): #c can be changed to any character
            print("\tCopying this one to target1")
            shutil.copyfile(input_images_path+images_list[index],output_images_path1 +images_list[index])
        if key == ord('t'):
            print("\tCopying this one to target2")
            shutil.copyfile(input_images_path+images_list[index],output_images_path2 +images_list[index])
        elif key == 2424832:  #right key
            index -= 1
        elif key == 2555904:  #left key
            index +=1
        elif key == ord('q'): #exit software
            break

        cv2.destroyAllWindows()
