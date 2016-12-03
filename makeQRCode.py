import numpy as np
import cv2
import sys

# command line inputs: placement, x coordinate, y coordinate, direction
# Creates a 8x8 pixel image for the QR Code in accordance to the guidelines specified on https://confluence.cornell.edu/display/CCRT/QR+Code+Data+Encoding

def makeCode(placement, x, y, direction):
	image = np.full((2400,2400), 256, dtype=float)

	image[0:1500, 0:1500] = 0
	image[300:1200, 300:1200] = 256
	image[600:900, 600:900] = 0
	image[1800:2100, 1800:2100] = 0
	image[2100:2400, 2100:2400] = 0

	# Constructing the image file name
	img_name = "QRCode-"

	# Getting the placement of the QR Code
	if placement == "wall":
		image[1800:2100, 0:300] = 0
		image[0:300, 1800:2100] = 0
		img_name += "wall-"
	else:
		image[2100:2400, 0:300] = 0
		image[0:300, 2100:2400] = 0
		img_name += "pillar-"

	# Getting the x location of the Code
	img_name += (str(x) + "-")
	if x >= 8:
		image[1800:2100, 300:600] = 0
		image[300:600, 1800:2100] = 0
		x -= 8
	if x >= 4:
		image[1800:2100, 600:900] = 0
		image[600:900, 1800:2100] = 0
		x -= 4
	if x >= 2:
		image[1800:2100, 900:1200] = 0
		image[900:1200, 1800:2100] = 0
		x -= 2
	if x >= 1:
		image[1800:2100, 1200:1500] = 0
		image[1200:1500, 1800:2100] = 0
		x -= 1

	#Getting the y location of the Code
	img_name += (str(y) + "-")
	if y >= 8:
		image[2100:2400, 300:600] = 0
		image[300:600, 2100:2400] = 0
		y -= 8
	if y >= 4:
		image[2100:2400, 600:900] = 0
		image[600:900, 2100:2400] = 0
		y -= 4
	if y >= 2:
		image[2100:2400, 900:1200] = 0
		image[900:1200, 2100:2400] = 0
		y -= 2
	if y >= 1:
		image[2100:2400, 1200:1500] = 0
		image[1200:1500, 2100:2400] = 0
		y -= 1

	# Getting the direction the code is facing
	if direction == 'S':
		image[1500:1800, 1800:2100] = 0
		image[1800:2100, 1500:1800] = 0
	elif direction == 'W':
		image[1500:1800, 1800:2400] = 0
		image[1800:2400, 1500:1800] = 0
	elif direction == 'E':
		image[1500:1800, 2100:2400] = 0
		image[2100:2400, 1500:1800] = 0
	img_name += direction

	img_name += ".png"

	# Make the image file and display it briefly
	cv2.imwrite(img_name, image)
	cv2.imshow('what', image)
	cv2.waitKey(1000)

if __name__ == "__main__":
	makeCode(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
