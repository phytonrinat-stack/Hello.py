import pygame

pygame.init()

windows=pygame.display.set_mode((1000,1000))

running=True

while running:

		for event in pygame.event.get():

				if event.type==pygame.QUIT:

						running=False

		windows.fill((255,255,255))

		pygame.display.flip()

pygame.quit()
