# Emojifier

Emojifier is a CLI python3 application to replace pixels in an image with emojis. 

## Dependencies

- Python 3.x
- numpy 1.21.2
- Pillow 8.3.2

## How to use it

Make sure you have all the dependencies within the python environment you are using. Run ```python3 emojifier.py```. It will ask you for input filename. Write the path to the file you want to emojify. Then the program asks you for output filename. Write the desired output file path. If left empty, the default input file is the palette emoji from the emoji folder and default output file is ```./testx.png```.

## What is in the code

Emojifier uses 1NN to compare the RGBA color vector of each pixel in the input image to the average RGBA vector of each emoji. The emoji is then placed into the output image. Since each emoji is 64x64 pixels in size, it is recommended to downscale the input image. Images with each side being at most 147 pixels have been tested to work, but with small changes to the code the user can try to create emojified versions of even larger images. 

## External sources

The emoji images are from [gemoji](https://github.com/github/gemoji).
