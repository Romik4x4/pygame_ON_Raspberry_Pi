#!/usr/bin/python

import os
import pygame
import time
import random
import math

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
adcColor = (255, 255, 0)
PI = 3.141592653

size = (320,240)
screen = pygame.display.set_mode(size)
borderColor = (255, 255, 255)
lineColor = (64, 64, 64)
subDividerColor = (128, 128, 128)
pygame.draw.rect(screen, borderColor, (8,28,312,212), 2)

def mymap(x,in_min,in_max,out_min,out_max):
	return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

MainLoop = True

while MainLoop:
	yLast = 238
	for x in range(3,317):
		y = int(math.sin(x))
		y = mymap(y,0,1,3,237)
		print "%d %d\r\n" % (x,y)
		pygame.draw.line(screen, adcColor, (x, yLast), (x+1, y))
		yLast = y
		pygame.display.update()
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
		MainLoop = False

pygame.quit()
