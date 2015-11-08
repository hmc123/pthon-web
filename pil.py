#pil.py
#!usr\bin\env python
# -*- coding: gb18030 -*-
__anthor__ = 'HMC'

'this is test about PIL'

#from PIL import Image, ImageFilter


#########################################
#im = Image.open('E:\wwww.jpg')
#w, h = im.size

#im2 = im.filter(ImageFilter.BLUR)
#im2.save('C:\Users\Administrator\Desktop\kkkkk.jpg','jpeg')
##########################################
__anthor = 'HMC'

'this is a test about PIL ,image operation'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

#random char
def randChar():
	return chr(random.randint(65,90))

#random color1
def randomColor():
	return (random.randint(0,225),random.randint(0,225),random.randint(0,225))

#random color2
def randomColor2():
	return (random.randint(150,225),random.randint(150,225),random.randint(150,225))


#create image  240*60
width = 240
height = 60
image = Image.new('RGB',(width, height),(255,0,255))

#create font
font = ImageFont.truetype('arial.ttf', 36)

#create drawa
draw = ImageDraw.Draw(image)

#fill every pixel
for i in range(width):
	for j in range(height):
		draw.point((i, j), fill = randomColor())

#draw word
for i in range(4):
	draw.text((60 * i + 10, 10),randChar(), font = font, fill = randomColor2())

# blur
image = image.filter(ImageFilter.BLUR)
image.save('C:\Users\Administrator\Desktop\hmc.jpg','jpeg')
