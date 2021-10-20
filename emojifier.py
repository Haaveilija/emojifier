# emojifier.py
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

EMOJI_SIZE = 64

def avg_color(imgarray):
	return np.mean(imgarray,axis=(0,1))


def avg_colors(list_of_imgarrays):
	print("Calculating average colors of emojis")
	avg_array = []
	n = 1
	for imgarray in list_of_imgarrays:
		avg_array.append(avg_color(imgarray))
		print(n, end='\r')
		n += 1
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
	print("Start creating image")
	print("Output image width:",width*EMOJI_SIZE)
	print("Output image height:",height*EMOJI_SIZE)
	print("Output image pixels:",width*height*EMOJI_SIZE*EMOJI_SIZE)
	im = Image.new("RGBA", (width*EMOJI_SIZE, height*EMOJI_SIZE), color)
	print("Created background for output image")
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


def best_emoji_index_for_color(color,avg_colors_of_emojis):
	smallest_dist = float('infinity')
	smallest_index = 0
	i = 0
	for emoji_color in avg_colors_of_emojis:
		dist = np.linalg.norm(color-emoji_color)
		#print("Comparing image to emoji no.",i,"distance:",dist)
		if dist < smallest_dist:
			smallest_dist = dist
			smallest_index = i
		i += 1
	return smallest_index


def print_emojis_with_avg_colors(emojis,avg_colors_of_emojis):
	# create background
	bg_width = 29
	bg_height = 30
	im = create_image(bg_width,bg_height)

	# insert emojis
	clr = (10,100,100,256)
	test_im = emojis[125] + emojis[12]
	test_im = np.asarray(create_image(1,1,clr))
	i = best_emoji_index(test_im, emojis)
	print(i)
	i = 0
	j = 0
	for x in range(bg_width):
		for y in range(bg_height):
			position = (x*EMOJI_SIZE,y*EMOJI_SIZE)
			#clr = (int(avg_colors_of_emojis[i][0]),int(avg_colors_of_emojis[i][1]),int(avg_colors_of_emojis[i][2]),int(avg_colors_of_emojis[i][3]))
			clr = (int(avg_colors_of_emojis[i][0]),int(avg_colors_of_emojis[i][1]),int(avg_colors_of_emojis[i][2]),255)
			test_im = np.asarray(create_image(1,1,clr))
			image = Image.fromarray(test_im)
			if i < len(emojis)-1:
				i += 1
			im.paste(image, position, image)

			image = Image.fromarray(emojis[j])
			if j < len(emojis)-1:
				j += 1				
			im.paste(image, position, image)
	im.show()
	im.save("./test/test.png", format="png")


def print_image_with_emojis(image, emojis, avg_colors_of_emojis):
	print("Create background")
	shp = image.shape
	bg_width = shp[1]
	bg_height = shp[0]
	print("width,height",bg_width,bg_height)
	
	im = create_image(bg_width,bg_height)

	print("Start processing")
	for x in range(bg_width):
		for y in range(bg_height):
			position = (x*EMOJI_SIZE,y*EMOJI_SIZE)
			i = best_emoji_index_for_color(image[y,x], avg_colors_of_emojis)
			em = Image.fromarray(emojis[i])
			im.paste(em, position, em)
			print(f'Processing pixel: ({x},{y})    ',end='\r')
	#im.show()
	im.save("./testx.png", format="png")


def main():
	print('Starting emojifier')
	emojis = load_emojis()
	avg_colors_of_emojis = avg_colors(emojis)
	input_file = input("Enter filename: ")
	#test_image = np.asarray(Image.open(input_file).convert("RGBA").resize((147,93))) # width, height
	test_image = Image.open(input_file).convert("RGBA")
	width = test_image.size[0]
	height = test_image.size[1]
	print("test image size", width, height)
	if width <= 147 and height < 147:
		pass
	elif width >= height:
		test_image = test_image.resize((147, (147/width)*height))
	elif height < width:
		test_image = test_image.resize(((147/height)*width,147))
	test_image = np.asarray(test_image)
	#test_image = emojis[82]
	#test_image = emojis[best_emoji_index(test_image, emojis)]
	print_image_with_emojis(test_image, emojis, avg_colors_of_emojis)


main()
