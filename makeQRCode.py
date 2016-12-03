import numpy as np
import cv2

# Creates a 8x8 pixel image for the QR Code in accordance to the guidelines specified on https://confluence.cornell.edu/display/CCRT/QR+Code+Data+Encoding

image = np.full((800,800), 256, dtype=float)

image[0:500, 0:500] = 0
image[100:400, 100:400] = 256
image[200:300, 200:300] = 0
image[600:700, 600:700] = 0
image[700:800, 700:800] = 0

# Constructing the image file name
img_name = "QRCode-"

# Getting the placement of the QR Code
placement = raw_input("Is the QR Code on a 'wall' or a 'pillar'? ")
invalid_input = not (placement == "wall" or placement == "pillar")
while (invalid_input):
	placement = raw_input("Valid entries are 'wall' or 'pillar'. Where is the QR Code to be placed? ")
	invalid_input = not (placement == "wall" or placement == "pillar")
if placement == "wall":
	image[600:700, 0:100] = 0
	image[0:100, 600:700] = 0
	img_name += "wall-"
else:
	image[700:800, 0:100] = 0
	image[0:100, 700:800] = 0
	img_name += "pillar-"

# Getting the x location of the Code
x = input("What is the x-coordinate of the QR Code? ")
invalid_input = x >= 16 or not type(x) == int
while (invalid_input):
	x = input("Valid entries must be integers less than 16. What is the x-coordinate of the QR Code? ")
	invalid_input = x >= 16 or not type(x) == int
img_name += (str(x) + "-")
if x >= 8:
	image[600:700, 100:200] = 0
	image[100:200, 600:700] = 0
	x -= 8
if x >= 4:
	image[600:700, 200:300] = 0
	image[200:300, 600:700] = 0
	x -= 4
if x >= 2:
	image[600:700, 300:400] = 0
	image[300:400, 600:700] = 0
	x -= 2
if x >= 1:
	image[600:700, 400:500] = 0
	image[400:500, 600:700] = 0
	x -= 1

#Getting the y location of the Code
y = input("What is the y-coordinate of the QR Code? ")
invalid_input = y >= 16 or not type(y) == int
while (invalid_input):
	y = input("Valid entries must be integers less than 16. What is the y-coordinate of the QR Code? ")
	invalid_input = y >= 16 or not type(y) == int
img_name += (str(y) + "-")
if y >= 8:
	image[700:800, 100:200] = 0
	image[100:200, 700:800] = 0
	y -= 8
if y >= 4:
	image[700:800, 200:300] = 0
	image[200:300, 700:800] = 0
	y -= 4
if y >= 2:
	image[700:800, 300:400] = 0
	image[300:400, 700:800] = 0
	y -= 2
if y >= 1:
	image[700:800, 400:500] = 0
	image[400:500, 700:800] = 0
	y -= 1

# Getting the direction the code is facing
direction = raw_input("What is the direction (N,S,E,W) of this QR Code? ")
invalid_input = not (direction == 'N' or direction == 'S' or direction == 'E' or direction == 'W')
while (invalid_input):
	direction = raw_input("Valid entries are 'N', 'S', 'E', or 'W'. What is the direction of this QR Code? ")
	invalid_input = not (direction == 'N' or direction == 'S' or direction == 'E' or direction == 'W')
if direction == 'E':
	image[500:600, 600:700] = 0
	image[600:700, 500:600] = 0
	img_name += "E"
elif direction == 'S':
	image[500:600, 600:800] = 0
	image[600:800, 500:600] = 0
	img_name += "S"
elif direction == 'W':
	image[500:600, 700:800] = 0
	image[700:800, 500:600] = 0
	img_name += "W"
else:
	img_name += "N"

img_name += ".jpg"

# Make the image file and display it briefly
cv2.imwrite(img_name, image)
cv2.imshow('what', image)
cv2.waitKey(1000)