#!/usr/bin/python

import os, syslog
import pygame
import time
import pywapi
import string
import os
from daemon import *

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

logo = pygame.image.load('/home/romik/img/01.png');
screen.blit(logo, (0, 0))
pygame.display.update()

ok = True
time.sleep(1)
