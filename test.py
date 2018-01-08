import sys
import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Square fun.")
pos_x = 300
pos_y = 250
vel_x = 0
vel_y = 0
color_change = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if vel_x < 6:
                    vel_x += 1
            elif event.key == K_LEFT:
                if vel_x > -6:
                    vel_x -= 1
        else:
            if not vel_x == 0:
                if vel_x > 0:
                    vel_x -= 1
                if vel_x < 0:
                    vel_x += 1
    screen.fill((0,0,200))
    #move rectangle
    pos_x += vel_x
    #keep rectangle on screen and change colour
    if pos_x > 450 or pos_x < 0:
        vel_x = -vel_x
        color_change = True
        color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    if pos_y > 450 or pos_y < 0:
        vel_y = -vel_y
        color_change = True
        color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    #draw rectangle
    if not color_change:
        color = 255,255,0
    width = 0 #solid fill
    pos = pos_x, pos_y, 50, 50
    pygame.draw.rect(screen, color, pos, width)
    pygame.display.update()