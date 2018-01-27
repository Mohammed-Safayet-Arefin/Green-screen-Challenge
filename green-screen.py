#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 23:14:44 2017

@author: safayetarefin
"""

import PIL
from PIL import Image
from matplotlib.colors import rgb_to_hsv


# Load image

img = Image.open("green1.png")


# Converting the image into RGBA so that it can have alpha channel
img = img.convert('RGBA')

#get the pixels of the image
pix_data = img.load()

#size of the image
x, y = img.size

## Predetermined range or threshold for GREEEN color in HSV

GREEN_RANGE_MIN_HSV = (100, 100, 100)
GREEN_RANGE_MAX_HSV = (200, 255, 255)

# Consider all pixels and turn each 'green' pixel to transparent

for i in range(x):

    for j in range(y):

        r, g, b, alpha = pix_data[i, j]

        #The R,G,B values are divided by 255 to change the range from 0..255 to 0..1
        # RGB values are normalized to values between 0 and 1

        arr = [r / 255.0, g / 255.0, b / 255.0]

        #converting RGB to HSV for getting the color information from the imgage intensity

        h_value, s_value, v_value = rgb_to_hsv(arr)


        h, s, v = (h_value * 360, s_value * 255, v_value * 255)

        min_h, min_s, min_v = GREEN_RANGE_MIN_HSV
        max_h, max_s, max_v = GREEN_RANGE_MAX_HSV

        if min_h <= h <= max_h and min_s <= s <= max_s and min_v <= v <= max_v:

            #putting ALPHA = 0 making the background transparent

            pix_data[i, j] = (0,0,0,0)


#saving the mask image

img.save("mask.png")

#Load mask image
mask_img = Image.open("mask.png")

#load original image
#original_img = Image.open("original-1.png")
original_img = Image.open("original-2(<x).png")
#original_img = Image.open("original-3(<y).png")
#original_img = Image.open("original-4(<x,<y).png")


#print the size of mask and original image
print ("Original image size: ", original_img.size)
print ("mask image size:", mask_img.size)


#setting original's coordinate system to 0,0 according to the python Imaging Library
#where the top-left of the green-screen mask image will be placed
#you can play with the location by changing the values
x_coordinate = 0
y_coordinate = 0


#getting the size of mask image and original image for comaprison
x_pix_original, y_pix_original = original_img.size
x_pix_mask, y_pix_mask = mask_img.size


#### MASK Image resizing so that it always fits in
#case-1
if x_pix_original > x_pix_mask and y_pix_original > y_pix_mask:

    print ("Original image is bigger than the mask image! so superimpose is done!No resizing")
    original_img.paste(mask_img, (x_coordinate, y_coordinate), mask_img)
    original_img.save("final-1.png")
    original_img.show()

#case-2
elif x_pix_original < x_pix_mask and y_pix_original > y_pix_mask:
    resize_mask_img = img.resize((x_pix_original,y_pix_mask), PIL.Image.ANTIALIAS)
    original_img.paste(resize_mask_img, (x_coordinate, y_coordinate), resize_mask_img)
    print ("Width of Mask image is bigger than the original image!Resizing and superimposing is done!")
    original_img.save("final-2.png")
    original_img.show()

#case-3
elif x_pix_original > x_pix_mask and y_pix_original < y_pix_mask:
    resize_mask_img = img.resize((x_pix_mask, y_pix_original), PIL.Image.ANTIALIAS)
    original_img.paste(resize_mask_img, (x_coordinate, y_coordinate), resize_mask_img)
    print ("Height of Mask image is bigger than the original image! Resizing and superimposing is done!")
    original_img.save("final-3.png")
    original_img.show()

#case-4
else:

    resize_mask_img = img.resize((original_img.size), PIL.Image.ANTIALIAS)
    original_img.paste(resize_mask_img, (x_coordinate, y_coordinate), resize_mask_img)
    print ("Mask image is bigger than the original image! Resizing and superimposing is done!!")
    original_img.save("final-4.png")
    original_img.show()


