import pygame,sys
import os
from pygame.locals import *

pygame.init()
displaySurf = pygame.display.set_mode((600, 600))
pygame.display.set_caption('mouse event')

isrunning = True

img = pygame.image.load("cat.png")
imgRect = img.get_rect()
imgRect.centerx =  300
imgRect.centery = 300

mx=300
my=300

blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
background = white

os.system('clear')
os.system('setterm -cursor off')
pygame.mouse.set_visible(False)

while isrunning:
	displaySurf.fill(background)
	for event in pygame.event.get():
		if event.type == QUIT:
			isrunning = False
		elif event.type == MOUSEMOTION:
			(mx,my) = event.pos
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				background = red
			if event.button == 3:
				background = green
			if event.button == 2:
				background = blue
		elif event.type == MOUSEBUTTONUP:
			background = white
	imgRect.centerx = mx
	imgRect.centery = my
	displaySurf.blit(img,imgRect)

	pygame.display.update()

pygame.quit()

os.system('setterm -cursor on')
