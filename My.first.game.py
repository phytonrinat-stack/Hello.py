import pygame
pygame.init()
windows=pygame.display.set_mode((1000,1000)) 
running=True
x=200
y=200
h=100
g=100
clock=pygame.time.Clock()
speed=10
color=(255,145,145)
collor=(145,255,0)
colour=(255,0,255)
collorr=(255,255,255)
while running:
	click=pygame.mouse.get_pos()	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
	clock.tick(60)
	windows.fill(collorr)
	pygame.draw.rect(windows,colour,(200,700,100,100))
	pygame.draw.rect(windows,colour,(400,700,100,100))
	pygame.draw.rect(windows,colour,(300,600,100,100))
	pygame.draw.rect(windows,colour,(300,800,100,100))
	if pygame.mouse.get_pressed()[0]:
		if click[0]>200 and click[0]<300 and click[1]>700 and click[1]<800:
			x=x-speed
		if click[0]>400 and click[0]<500 and click[1]>700 and click[1]<800:
			x=x+speed
		if click[0]>300 and click[0]<400 and click[1]>600 and click[1]<700:
			y=y-speed			
		if click[0]>300 and click[0]<400 and click[1]>800 and click[1]<900:
			y=y+speed		
	pygame.draw.rect(windows,color,(x,y,h,g))
	pygame.display.flip()
