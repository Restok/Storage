import pygame as pg
import random
# this program will create a game window and draw a green circle

#initialize the pygame modules
pg.init()

#creates a surface(game window) set mode defines width height
screen = pg.display.set_mode([800,600])

keep_going = True

GREEN = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
RED = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
myClock = pg.time.Clock()
radius = random.randint(30, 70)
radius2 = random.randint(30, 70)
onex = 100.
oney = 100.
twox = 500.
twoy = 500.
speed = 400
speed2 = 400
count = 0
changeRedDirection = False
def bounce():
	global onex, oney, rspeed, rspeed2, radius
while keep_going:
		#gets all game events
	for event in pg.event.get():
		if event.type == pg.QUIT:
			keep_going = False
	#draws the circle
	#SURFACE, COLOR, POS, RADIUS
	GREEN = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	circ = pg.draw.circle(screen, GREEN, (int(onex),int(oney)), radius)
	timepassed = myClock.tick()
	timePassedSeconds = timepassed/1000
	rspeed = random.randint(0,4000)
	rspeed2 = random.randint(0,4000)
	distancemoved = timePassedSeconds*rspeed
	distancemoved2 = timePassedSeconds*rspeed2
	print(distancemoved)
	onex+=distancemoved
	oney+=distancemoved2
	if onex > 200:
		rspeed = random.randint(0,4000)
		rspeed2 = random.randint(0,4000)
		distancemoved = timePassedSeconds*rspeed
		distancemoved2 = timePassedSeconds*rspeed2
		onex -= distancemoved
		oney -= distancemoved
	if onex < 0:
		rspeed = random.randint(0,4000)
		rspeed2 = random.randint(0,4000)
		distancemoved = timePassedSeconds*rspeed
		distancemoved2 = timePassedSeconds*rspeed2
		onex += distancemoved
		oney += distancemoved
	if oney > 300:
		rspeed = random.randint(0,4000)
		rspeed2 = random.randint(0,4000)
		distancemoved = timePassedSeconds*rspeed
		distancemoved2 = timePassedSeconds*rspeed2
		onex -= distancemoved
		oney -= distancemoved
	if onex < 0:
		rspeed = random.randint(0,4000)
		rspeed2 = random.randint(0,4000)
		distancemoved = timePassedSeconds*rspeed
		distancemoved2 = timePassedSeconds*rspeed2
		onex += distancemoved
		oney += distancemoved

	pg.display.update()
"""	if onex < 0 and oney <0:
		changeRedDirection = True
	if onex > 1920 and oney > 1080:
		changeRedDirection = False
	if changeRedDirection == True:
		onex += reddistancemoved
		oney += reddistancemoved
	else:
		onex -= reddistancemoved
		oney -= reddistancemoved"""