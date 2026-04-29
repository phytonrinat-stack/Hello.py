import pygame
pygame.init()
windows=pygame.display.set_mode((1000,1000))
x=0
clock=pygame.time.Clock()
color=(255,0,255)
z=0
a=10
y=10
running=True
while running:
	z=z+a
	if z==1250:
		a=(-10)
	if z==0:
		a=10
	x=x+y
	if x==650:
		y=(-10)
	if x==0:
		y=10
	for event in pygame.event.get():
		if type==pygame.QUIT:
			running=False
	windows.fill((0,255,0))
	clock.tick(60)
	pygame.draw.rect(windows,color,(x,z,110,110))
	pygame.display.flip()
	
	
	

										#hello world 1.6.
