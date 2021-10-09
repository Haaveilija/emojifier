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
		image = Image.open(emojipath+file)
		data = asarray(image)
		emojis.append(data)
	#print("emoji shape:",data.shape)
	#print(len(emojis))
	print(f'Loaded {len(emojis)} emojis of shape {data.shape}.')

	imtest = Image.fromarray(data)
	#image.show()
	width = 16
	height = 16
	im = Image.new("RGB", (width*EMOJI_SIZE, height*EMOJI_SIZE), (0,0,0))
	image = Image.fromarray(data)
	position = (0,0)
	im.paste(image, position, image)
	im.show()
main()
