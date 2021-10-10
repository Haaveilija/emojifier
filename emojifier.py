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


def create_image(width,height, color=(0,0,0)):
	im = Image.new("RGBA", (width*EMOJI_SIZE, height*EMOJI_SIZE), color)
	return im


def best_emoji_index(im,emojis):
	smallest_dist = float('infinity')
	smallest_index = 0
	i = 0
	for em in emojis:
		dist = np.linalg.norm(im-em)
		print("Comparing image to emoji no.",i,"distance:",dist)
		if dist < smallest_dist:
			smallest_dist = dist
			smallest_index = i
		i += 1
	return smallest_index



def main():
	print('Starting emojifier')
	emojis = load_emojis()
	avg_colors_of_emojis = avg_colors(emojis)
	print(len(avg_colors_of_emojis))

	# create background
	bg_width = 16
	bg_height = 16
	im = create_image(bg_width,bg_height)

	# insert emojis
	clr = (10,100,100,256)
	test_im = emojis[125] + emojis[12]
	test_im = np.asarray(create_image(1,1,clr))
	i = best_emoji_index(test_im, emojis)
	print(i)
	k = True
	for x in range(bg_width):
		for y in range(bg_height):
			if k:
				image = Image.fromarray(test_im)
				position = (x*EMOJI_SIZE,y*EMOJI_SIZE)
				im.paste(image, position, image)
				k = False
				continue
			image = Image.fromarray(emojis[i])
			#image = Image.fromarray(test_im)
			position = (x*EMOJI_SIZE,y*EMOJI_SIZE)
			im.paste(image, position, image)
	#image = Image.fromarray(data)
	#position = (0,0)
	#im.paste(image, position, image)
	im.show()
	im.save("./test/test.png", format="png")


main()
