#!/usr/bin/python

import os, syslog
import pygame
import time
import pywapi
import string
import os

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.display.init()
size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen.fill((0, 0, 0))        
pygame.font.init()
pygame.display.update()
pygame.mouse.set_visible(False)
fontpath = pygame.font.match_font('dejavusansmono')
font = pygame.font.Font(fontpath, 20)
fontSm = pygame.font.Font(fontpath, 18)

logo = pygame.image.load('/home/romik/img/01.png')
screen.blit(logo, (0, 0))
pygame.display.update()

ok = True
time.sleep(1)

for dirname, dirnames, filenames in os.walk('/home/romik/img/'):
    # print path to all filenames.
    for filename in filenames:
       png = os.path.join(dirname, filename)
       logo = pygame.image.load(png)
       screen.blit(logo, (0, 0))
       pygame.display.update()
       time.sleep(2)
       screen.fill((0, 0, 0))
       pygame.display.update()




