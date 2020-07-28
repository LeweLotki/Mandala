import pygame
import math

n=int(input('Enter the quantity of axes: '))

pygame.init()

sqr=pygame.image.load('images/sqr.png')
sqr=pygame.transform.scale(sqr, (10,10))

def rotatePoint(centerPoint,point,angle):
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

class points:
    def __init__(self, positionx,positiony,n):
        self.x=positionx
        self.y=positiony
        self.i=n
        self.n=n
    def render(self,Image):
        while self.i>0:
            a=int(rotatePoint((400,400),(self.x,self.y),(self.n-self.i)*(360/self.n))[0])
            b=int(rotatePoint((400,400),(self.x,self.y),(self.n-self.i)*(360/self.n))[1])
            screen.blit(Image,(a,b))
            self.i-=1
        self.i=self.n

        
points_list=[]

bl = (  0,   0,   0)
w = (255, 255, 255)
b =  (  0,   0, 255)
g = (  0, 240,   0)
r =   (255,   0,   0)
gr=(200,200,200)
y=(255,255,0)
o=(255,140,0)

size = [800,800]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("simple game")

done=False
clock=pygame.time.Clock()

while not done:
    key=pygame.key.get_pressed()
    mousex=pygame.mouse.get_pos()[0]
    mousey=pygame.mouse.get_pos()[1]
    key=pygame.key.get_pressed() 
    clock.tick(200)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True
    
    if key[pygame.K_c]:
       points_list.clear()
    
    if pygame.mouse.get_pressed()[0]: #and mousex>400 and mousey>400:
       #print(mousex,mousey)
       points_list.append(points(mousex,mousey,n))
    
    screen.fill(w)
    
    for val in points_list:
        val.render(sqr)
        
    pygame.display.flip()
    
pygame.quit()
