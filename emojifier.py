# emojifier.py
from PIL import Image
from numpy import asarray
import os
import cv2
import matplotlib.pyplot as plt

EMOJI_SIZE = 64

def main():
	print('Starting emojifier')
	print('Loading emojis')
	emojipath = "./emoji/"
	inputlist = os.listdir(emojipath)
	emojis = []
	for file in inputlist:
		#print(emojipath + file)
		image = Image.open(emojipath+file).convert("RGBA")
		data = asarray(image)
		emojis.append(data)
	#print("emoji shape:",data.shape)
	#print(len(emojis))
	print(f'Loaded {len(emojis)} emojis of shape {data.shape}.')

	imtest = Image.fromarray(data)
	#image.show()
	width = 16
	height = 16
	im = Image.new("RGBA", (width*EMOJI_SIZE, height*EMOJI_SIZE), (0,0,0))
	i = 0
	for x in range(width):
		for y in range(height):
			image = Image.fromarray(emojis[i])
			position = (x*EMOJI_SIZE,y*EMOJI_SIZE)
			im.paste(image, position, image)
			i += 1
	#image = Image.fromarray(data)
	#position = (0,0)
	#im.paste(image, position, image)
	im.show()
	im.save("./test/test.png", format="png")


main()
