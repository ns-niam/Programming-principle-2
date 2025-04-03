import pygame

pygame.init()

screen = pygame.display.set_mode((840,473))
pygame.display.set_caption("Player")
clock = pygame.time.Clock()
pygame.mixer.init()
running = True
screen.fill((0,0,0))
fon = pygame.image.load("fon.jpg")
screen.blit(fon,(0,0))
pygame.display.flip()
paused = False
current = 0
def handler():
    global current, paused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                    current = (current + 1) % len(playlist)
                    start_playing(playlist, current)
            elif event.key == pygame.K_p:
                    current = (current - 1) % len(playlist)
                    start_playing(playlist, current)    
            elif event.key == pygame.K_SPACE:
                 paused = not paused
                 if paused:
                      pygame.mixer.music.pause() 
                 else:
                      pygame.mixer.music.unpause()
                 
    return True

def create_playlist(pl : list, music : str) -> None:
    pl.append(music)

def start_playing(playlist, n = 0):
    if playlist:
        pygame.mixer.music.load(playlist[n])
        pygame.mixer.music.play()
    else:
        print("Playlist not")

playlist = []

create_playlist(playlist, "music.mp3")
create_playlist(playlist, "musix.mp3")


start_playing(playlist)

while running:
    clock.tick(60)
    running = handler()
