import pygame

pygame.init()
running = True
WIDTH, HEIGHT = 1200, 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

#All shapes
rectangular = pygame.Rect(10, 10, 20, 10)
circle_radius = 10
circle_center = (50, 20)
pos = (1200, 800)

#Colors
blue = pygame.Rect(1090, 10, 20, 20)
red = pygame.Rect(1130, 10, 20, 20)
green = pygame.Rect(1170, 10, 20, 20)

color = "white"
shape = "rectangular"

eraser = pygame.image.load("eraser.png")
eraser_rect = eraser.get_rect()
eraser_rect.center = (1050, 15)

do_draw = False
drawings = []  #The "memory" of Paints.

# Handler of events
def handler():
    global pos, do_draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                do_draw = True
                pos = pygame.mouse.get_pos()   
        if event.type == pygame.MOUSEMOTION:
            if do_draw:
                pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            do_draw = False
    return True

#Draw menu
def menu():
    pygame.draw.aaline(screen, "black", (0, 40), (1200, 40))
    pygame.draw.rect(screen, "black", rectangular)
    pygame.draw.circle(screen, "black", circle_center, circle_radius)
    screen.blit(eraser, eraser_rect.center)
    pygame.draw.rect(screen, "blue", blue)
    pygame.draw.rect(screen, "red", red)
    pygame.draw.rect(screen, "green", green)

    

def choose_shape(pos):
    global shape
    if rectangular.collidepoint(pos):
        shape = "rectangular"
    elif ((circle_center[0] - pos[0])**2 + (circle_center[1] - pos[1])**2) <= circle_radius**2:
        shape = "circle"
    elif eraser_rect.collidepoint(pos):
        shape = "rectangular"


def choose_color(pos):
    global color
    if red.collidepoint(pos):
        color = "red"
    if blue.collidepoint(pos):
        color = "blue"
    if green.collidepoint(pos):
        color = "green"
    if eraser_rect.collidepoint(pos):
        color = "white"

#After choosing color and shape, show it to the up middle point of the screen.
def active(color, shape):
    if shape == "rectangular":
        pygame.draw.rect(screen, color, (600, 10, 20, 10))
    elif shape == "circle":
        pygame.draw.circle(screen, color, (605, 18), 10)

#Drawing function. Take the active color and shape as arguments.
def drawing(color, shape, pos = pos):
    if pos[1] > 40:
        if shape == "rectangular":
            pygame.draw.rect(screen, color, [pos[0], pos[1], 20, 10])
        elif shape == "circle":
            pygame.draw.circle(screen, color, pos, 10)


# Game cycle
while running:
    clock.tick(FPS)
    screen.fill("white")
    running = handler()
    menu()
    choose_shape(pos)
    choose_color(pos)
    active(color, shape)
    
    for art in drawings:
        drawing(art[0], art[1], art[2])
    drawing(color, shape, pos)
    drawings.append((color, shape, pos))

    





    pygame.display.update()




pygame.quit()
