# emojifier.py
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

EMOJI_SIZE = 64

def avg_color(imgarray):
	return np.mean(imgarray, axis=(0,1))


def avg_colors(list_of_imgarrays):
	print("Calculating average colors of emojis")
	avg_array = []
	for imgarray in list_of_imgarrays:
		avg_array.append(avg_color(imgarray))
	return avg_array


def load_emojis():
	print('Loading emojis')
	emojipath = "./emoji/"
	#inputlist = sorted(os.listdir(emojipath))
	inputlist = os.listdir(emojipath)
	emojis = []
	for file in inputlist:
		image = Image.open(emojipath+file).convert("RGBA")
		data = np.asarray(image)
		emojis.append(data)

	print(f'Loaded {len(emojis)} emojis of shape {data.shape}.')
	return emojis


def main():
	print('Starting emojifier')
	emojis = load_emojis()
	avg_colors_of_emojis = avg_colors(emojis)

	# create background
	bg_width = 16
	bg_height = 16
	im = Image.new("RGBA", (bg_width*EMOJI_SIZE, bg_height*EMOJI_SIZE), (0,0,0))

	# insert emojis
	i = 0
	for x in range(bg_width):
		for y in range(bg_height):
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
