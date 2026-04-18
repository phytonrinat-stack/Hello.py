
#Hello world.py.1.5

import pygame

pygame.init()

windows=pygame.display.set_mode((1000,
1000))

points2=[(100,400),(600,400),(350,200)]

color2=(255,215,0)

color=(255,192,203)

points=[(100,900),(100,400),(600,400),(600,900)]

OpenAI=True

while OpenAI:

	for event in pygame.event.get():

			if event.type==pygame.QUIT:

					OpenAI=False

	windows.fill((255,255,255))

	pygame.draw.polygon(windows,color,points)

	pygame.draw.polygon(windows,color2,points2)

	pygame.display.flip()
