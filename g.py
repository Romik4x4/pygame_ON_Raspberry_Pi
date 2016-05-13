#!/usr/bin/python

import pygame
from pygame.locals import *
import os
from time import sleep

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((320, 240))
screen.fill((0,0,0))

circle_color = (0,0,255)
circle_pos = (10,30) 
circle_radius = 75 
circle_width = 0
pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)

rect_1_color = (255,0,255) 
rect_2_color = (0, 0, 255)
rect_1_rect = Rect((10,10),(100,100)) 
rect_2_rect = Rect((150,150),(300,100))
rect_1_width = 0 
rect_2_width = 4
pygame.draw.rect(screen, rect_1_color, rect_1_rect, rect_1_width) 
pygame.draw.rect(screen, rect_2_color, rect_2_rect, rect_2_width)

pygame.display.update()

MainLoop = True

while MainLoop:
    for event in pygame.event.get():
        if(event.type is MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            MainLoop = False

pygame.quit() 
