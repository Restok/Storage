#ORIGINAL
"""
import pygame
from pygame.locals import *
import random
import time
RED = (255,0,0)
pygame.init()
level = 1
cooldown = 1000
class test(pygame.sprite.Sprite):
	def __init__(self, w):
		super().__init__()
		self.image = pygame.Surface([600,600])
		self.rect = self.image.get_rect()
		self.image = pygame.image.load("index.png")
		self.image = pygame.transform.scale(self.image, (w,w))
		self.last = pygame.time.get_ticks()
screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background.fill([0,0,0])
rX = random.randint(0, 500)
rX2 = random.randint(0, 500) 
screen.blit(background, (0,0))
sp = []
all_sprites_list = pygame.sprite.Group()
a_1 = test(random.randint(40,60))
a_1.rect.x = rX
a_1.rect.y = -400
sp.append(a_1)
all_sprites_list.add(a_1)
a_2 = test(random.randint(40,60))
rX2 = random.randint(0, 500) 
a_2.rect.x = rX2
a_2.rect.y = -200
sp.append(a_2)
all_sprites_list.add(a_2)
a_3 = test(random.randint(40,60))
rX3 = random.randint(0, 500) 
a_3.rect.x = rX3
a_3.rect.y = -150
sp.append(a_3)
all_sprites_list.add(a_3)
a_4 = test(random.randint(40,60))
rX4 = random.randint(0, 500) 
a_4.rect.x = rX4
a_4.rect.y = -100
sp.append(a_4)
all_sprites_list.add(a_4)
a_5 = test(random.randint(40,60))
rX5 = random.randint(0, 500) 
a_5.rect.x = rX5
a_5.rect.y = -50
sp.append(a_5)
all_sprites_list.add(a_5)
a_6 = test(random.randint(40,60))
rX6 = random.randint(0, 500) 
a_6.rect.x = rX6
a_6.rect.y = -700
sp.append(a_6)
all_sprites_list.add(a_6)
print(a_6)
print(a_1)
Running = True
while Running:
	now = pygame.time.get_ticks()
	for x in sp:
		x.rect.y+=level
	m_pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == QUIT:
			Running = False
		if event.type == MOUSEBUTTONDOWN:
			for s in sp:
				if s.rect.collidepoint(m_pos):
					s.kill()
	pygame.display.flip()
	all_sprites_list.clear(screen, background)
	all_sprites_list.draw(screen)
	all_sprites_list.update()
	clock.tick(60)
"""
#IMPORVISED:
import pygame
import random

# --- classes --- (UpperCaseNames)

class Test(pygame.sprite.Sprite):

    def __init__(self, w):
        super().__init__()
        self.image = pygame.image.load("index.png")
        self.image = pygame.transform.scale(self.image, (w, w))
        self.rect = self.image.get_rect()
        self.last = pygame.time.get_ticks()
# --- main ----

level = 1

# - init -

pygame.init()
pygame.font.init()
text = pygame.font.SysFont("Arial", 50)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Don't let the apple hit the ground!")
# - items -
all_sprites_list = pygame.sprite.Group()

for x in range(10):
    item = Test(random.randint(50, 70))
    item.rect.x = 40 * random.randint(0, 10)
    item.rect.y = random.randint(-1300, -30)
    all_sprites_list.add(item)

bg = pygame.image.load("newton.jpg")
bg = pygame.transform.scale(bg, (600,600))
# - mainloop -
clock = pygame.time.Clock()
running = True
while running:
    for item in all_sprites_list:
        item.rect.y += (level+1)
        if item.rect.y >= 500:
        	textsurface = text.render("GAME OVER", False, (255, 0, 0))
       		print("You got to level", level)
       		running = False
    textsurface = text.render(f'LEVEL {level}', False, (0, 0, 0))
    screen.blit(bg, (0,0))
    screen.blit(textsurface,(225,225))
    all_sprites_list.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in all_sprites_list:
                if item.rect.collidepoint(event.pos):
                    item.kill()
    pos = 0, 350, 400, 400
    if len(all_sprites_list)==0:
	    for x in range(10):
	    	item = Test(random.randint(40, 60))
	    	item.rect.x = 40 * random.randint(0, 10)
	    	item.rect.y = random.randint(-700, -30)
	    	all_sprites_list.add(item)
	    level+=1
    pygame.display.flip()
    all_sprites_list.clear(screen, bg)
    all_sprites_list.update()
    clock.tick(30)
pygame.quit()