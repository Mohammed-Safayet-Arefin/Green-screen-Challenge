# Green-screen-Challenge

Given a sample image having a green screen as background, find out the green screen masked image
and superimpose it on another image to create a striking combination. 

The parameters are:
        • The green-screen masked image.
        • The original image’s coordination system, where the top-left of the green-screen image will be placed.
        • Resized the masked image so that it always fits into the original image whatever the size of the original image.

Implementation:
For solving this problem, I have used python as a programming language.

Python IDE:
For running this program, I have used “Anaconda-spyder” as an IDE. Pycharm can also be used as a Python IDE
in this case.

Python Library:
In this assignment, I have used python image processing library named “pillow” that provides image reading,
manipulation, and writing functionality for python. 

Code Analysis:

In my code, I follow the below steps:

	• Take the given “green1.png” image as an input.
    
	• Converted the given image into RGBA so that it can have alpha channel and it will help us to make the background of the given image transparent.
    
    • Defining the range or threshold values for the Green color for HSV.

    • Considered all the pixels of the given image and turn each Green pixel into transparent by making the alpha value zero “0”. If you change the alpha values, then the intensity will be changed. More the alpha value, more will be the full dark intensity. The range of alpha values is 0-255.

    • For doing the above step, I have converted the RGB values to the HSV values because RGB more correlated to color intensity or luminance. We can’t separate color information from the luminance. That’s why HSV is needed to separate color information from luminance. Again, HSV values are more efficient to find out the color pixel information then RGBA values. The range of Hue (H) is 0-360, Saturation (S) is 0-255, and range of Value (V) is 0-255.
    
    • Finally, after doing those steps I got the mask image and saved the mask image as “mask.png”
    
    • I loaded different sizes of the original images in my program in which I need to impose the mask image.
    
    • I have defined original image’s coordinate system to (0,0) according to the python Imaging Library where the top-left of the green-screen mask image will be placed. By changing those values, the location of the mask image on the original image will be changed.
    
    • For mask image resizing so that it can always fits in the original image, I have considered four cases. I have compared the height and width of the original image with the height and width of the mask image.
    
        o   Case 1: (Original image is greater than the Mask Image)
                    In this case, we don’t need to do any resizing. I have put the mask image on the original image according to the given coordinates values.
                    
        o Case 2: (Width of Mask image is bigger than the original image’s width)
                    In this case, I have resized the masked image according to the width of the original image and height of the of the mask image. 

        o Case 3: (Height of Mask image is bigger than the original image)
                In this case, I have resized the masked image according to the width of the mask image and height of the of the original image. 

        o Case 4: (Mask image is bigger than the original image)
                In this case, I have resized the masked image according to the width and height of the of the original image.


    • For all the cases, the aspect ratio of the mask image while resizing is handled by “PIL.Image.ANTIALIAS”. That’s why, while resizing no information of the mask image is lost.
