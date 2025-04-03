import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
running = True
screen.fill((255,255,255))
pygame.display.set_caption("Draw Circle")

pygame.display.flip()


def handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
x = 250
y = 250
  
width = 50
height = 50
  
vel = 20

while running:
    clock.tick(60)
    running = handler()
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x>0: 
        x -= vel    
    if keys[pygame.K_RIGHT] and x<500-width: 
        x += vel     
    if keys[pygame.K_UP] and y>=0: 
        y -= vel    
    if keys[pygame.K_DOWN] and y<=500-height: 
        y += vel 
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255, 0, 0), (x,y), 25) 

    pygame.display.flip()  

pygame.quit()
