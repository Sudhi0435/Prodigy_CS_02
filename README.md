# Prodigy_CS_02
# Task-02
Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images

# Pixel manipulation
The user can manipulate pixels, the basic unit of programmable color on a computer display or in a computer image. The user can erase, create, copy, and move pixels on a screen to show something different than it was originally was (erasing the pixels of a burglar on a video so he wont get caught)

How it works: 1.Load and Convert Image:

The image is opened from the specified input_path and converted to RGB mode if it isn't already in that mode. 2.Access Pixels:

The load method is used to get the pixel data of the image, allowing direct manipulation of pixel values. 3.Encrypt Pixels:

Iterate over each pixel using nested loops. For each pixel at coordinates (i, j), retrieve the RGB values. Encrypt each RGB component: Add the key to the red and green components and take modulo 256 to ensure the value stays within the 0-255 range. XOR the blue component with the key (bitwise operation). Set the new encrypted values back to the pixel. 4.Save Decrypted Image:

Save the modified image to the specified output_path.

# Repository Contents
PRODIGY_CS_02.py : The main Python script containing the implementation of the Pixel Manipulation.

README.md : This file, providing an overview of the task and the project.
