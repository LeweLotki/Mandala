import pygame

pygame.init()

class points:
    def __init__(self, positionx,positiony):
        self.x=positionx
        self.y=positiony
    def render(self):
        pygame.draw.rect(screen, bl, [self.x, self.y, 5, 5]) 
        pygame.draw.rect(screen, bl, [800-self.x, self.y, 5, 5]) 
        pygame.draw.rect(screen, bl, [self.x, 800-self.y, 5, 5]) 
        pygame.draw.rect(screen, bl, [800-self.x, 800-self.y, 5, 5]) 
        pygame.draw.rect(screen, bl, [self.y, self.x, 5, 5]) 
        pygame.draw.rect(screen, bl, [800-self.y, self.x, 5, 5]) 
        pygame.draw.rect(screen, bl, [self.y, 800-self.x, 5, 5]) 
        pygame.draw.rect(screen, bl, [800-self.y, 800-self.x, 5, 5]) 

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
    mousex=pygame.mouse.get_pos()[0]
    mousey=pygame.mouse.get_pos()[1]
    key=pygame.key.get_pressed() 
    clock.tick(200)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True
    
    if pygame.mouse.get_pressed()[0] and mousex>400 and mousey>400:
       #print(mousex,mousey)
       points_list.append(points(mousex,mousey))
    
    screen.fill(w)
    
    for n in points_list:
        n.render()
        
    pygame.display.flip()
    
pygame.quit()
