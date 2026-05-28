import pygame
pygame.init()
windows=pygame.display.set_mode((2000,2000))
#deyişenler
h=75
g=75
x_me=200
y_me=200
x_enemy=500
y_enemy=500
clock=pygame.time.Clock()
collor=(255,255,255)
colour=(255,0,255)
color=(255,0,255)
collour=(0,155,0)
fps=60
speed=6
enemy_speed=1
running=True
while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
	windows.fill(collor)
	pygame.draw.polygon(windows,colour,[(200,1250),(75,1175),(200,1100)])
	pygame.draw.polygon(windows,colour,[(350,1100),(350,1250),(475,1175)])
	pygame.draw.polygon(windows,colour,[(200,1100),(350,1100),(275,975)])
	pygame.draw.polygon(windows,colour,[(200,1250),(350,1250),(275,1375)])
	clock.tick(fps)
	click=pygame.mouse.get_pos()
	if pygame.mouse.get_pressed()[0]:
		if click[0]>75 and click[0]<200 and click[1]>1100 and click[1]<1250:
			x_me=x_me-speed
		if click[0]>350 and click[0]<475 and click[1]>1100 and click[1]<1250:
			x_me=x_me+speed
		if click[0]>200 and click[0]<350 and click[1]<1100 and click[1]>975:
			y_me=y_me-speed
		if click[0]>200 and click[0]<350 and click[1]>1250 and click[1]<1375:
			y_me=y_me+speed
	
	if x_enemy>x_me:
		x_enemy=x_enemy-enemy_speed
	if x_enemy<x_me:
		x_enemy=x_enemy+enemy_speed
	if y_enemy>y_me:
		y_enemy=y_enemy-enemy_speed
	if y_enemy<y_me:
		y_enemy=y_enemy+enemy_speed
	
	if x_me<0:
		x_me=675
	if x_me>675:
		x_me=0
	if y_me<0:
		y_me=915
	if y_me>915:
		y_me=0
		
	if x_me==x_enemy and y_me==y_enemy:
		running=False
			
	pygame.draw.polygon(windows,(0,0,0),[(0,950),(750,950),(750,970),(0,970)])
	pygame.draw.rect(windows,(255,0,0),(x_enemy,y_enemy,h,g))
	pygame.draw.circle(windows,(145,0,0),(x_enemy+20,y_enemy+15),(10))
	pygame.draw.circle(windows,(145,0,0),(x_enemy+55,y_enemy+15),(10))
	pygame.draw.polygon(windows,(145,0,0),[(x_enemy+10,y_enemy+55),(x_enemy+65,y_enemy+55),(x_enemy+65,y_enemy+65),(x_enemy+10,y_enemy+65)])
	pygame.draw.rect(windows,collour,(x_me,y_me,h,g))
	pygame.draw.circle(windows,(0,100,0),(x_me+20,y_me+15),(10))
	pygame.draw.circle(windows,(0,100,0),(x_me+55,y_me+15),(10))
	pygame.draw.polygon(windows,(0,100,0),[(x_me+10,y_me+55),(x_me+65,y_me+55),(x_me+65,y_me+65),(x_me+10,y_me+65)])
	pygame.draw.rect(windows,(0,100,0),(x_me+10,y_me+45,10,10))
	pygame.draw.rect(windows,(0,100,0),(x_me+55,y_me+45,10,10))
	
	pygame.display.flip()
pygame.quit()
