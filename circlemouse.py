import pygame
import random as rd
pygame.init()

class Circle(pygame.sprite.Sprite):
	def __init__(self, color, radius):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((radius*2, radius*2))
		self.image.fill((0, 0, 0))
#		pygame.draw.circle(self.image, color, (radius, radius), radius, 0)
		self.image = pygame.image.load("index.png")		
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.center = pygame.mouse.get_pos()

screen = pygame.display.set_mode([800, 600])
background = pygame.Surface(screen.get_size())
background.fill([0,0,0])
screen.blit(background, (0,0))
pygame.mouse.set_visible(False)
color = (255,0,0)
keepGoing = True
circle = Circle(color, 40)
while keepGoing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keepGoing = False
	allSprites = pygame.sprite.Group(circle)
	color = (rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
	allSprites.clear(screen, background)
	allSprites.update()
	allSprites.draw(screen)


	pygame.display.flip()