import pygame

pygame.init()

windows=pygame.display.set_mode((1000,1000))

clock=pygame.time.Clock()

pygame.display.set_caption("Rinat's project")
x=300

colour=(255,0,255)

y=400

w=60

speed=20

h=60

Running=True

while Running:
	
	for event in pygame.event.get():
		
		if event.type==pygame.QUIT:
			
			Running=False
			
	clock.tick(60)
	
	keys=pygame.key.get_pressed()
	
	windows.fill((0,145,255))
	
	if keys[pygame.K_LEFT]:
		x=x-speed
		
	if keys[pygame.K_RIGHT]:
		x=x+speed
		
	if keys[pygame.K_UP]:
		y=y-speed
		
	if keys[pygame.K_DOWN]:
		y=y+speed
		
	pygame.draw.rect(windows,colour,(x,y,w,h))
	
	if x>1000:
		x=0
		
	if x<0:
		x=1000
		
	if y>1000:
		y=0
		
	if y<0:
		y=1000
		
	pygame.display.flip()
