import pygame
from datetime import datetime

pygame.init()

#Screen config
screen_size = (829,836)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Clock")
screen.fill((0,0,0))
pygame.display.flip()

clock = pygame.time.Clock()

running = True

def handler() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
        
bg = pygame.image.load("images\clock.png")
center = screen.get_rect().center

hand_min = pygame.image.load("images\minute_hand.png")
hand_sec = pygame.image.load("images\seconds_hand.png")

while running:
    clock.tick(60)
    running = handler()
    time = datetime.now()
    
    min_rot = pygame.transform.rotate(hand_min, -(time.minute)*6)
    sec_rot = pygame.transform.rotate(hand_sec, -(time.second)*6)

    min_cent = min_rot.get_rect(center=center)
    sec_cent = sec_rot.get_rect(center=center)

    screen.blit(bg, (0,0))
    screen.blit(sec_rot, sec_cent)
    screen.blit(min_rot, min_cent)
    
    pygame.display.flip()
    

pygame.quit()

