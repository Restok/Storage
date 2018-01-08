import sys
import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode([600,600])

xpos = 200
ypos = 200
xvel = 0
yvel = 0

isrunning = True
colorchange = False
while isrunning:
	clock = pygame.time.Clock()
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == QUIT:
			isrunning = False
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				if xvel < 10:
					xvel+=8
			elif event.key == K_LEFT:
				if xvel > -10:
					xvel -=8
		else:	
			if not xvel == 0:
				if xvel > 0:
					xvel -=8
				if xvel < 0:
					xvel+=8
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				if yvel < 10:
					yvel+=8
			elif event.key == K_UP:
				if yvel > -10:
					yvel -=8
		else:	
			if not yvel == 0:
				if yvel > 0:
					yvel -=8
				if yvel < 0:
					yvel+=8

	screen.fill([0,0,0])
	xpos += xvel
	ypos += yvel

	if xpos >= 550 or xpos <= 0:
		xvel = -xvel
		colorchange = True
		color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
	if ypos >= 550 or ypos <= 0:
		yvel = -yvel
		colorchange = True
		color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
	if not colorchange:
		color = [255,255,255]
	fill = 0
	pos = xpos, ypos, 50, 50
	pygame.draw.rect(screen,color, pos, fill)
	pygame.display.update() 