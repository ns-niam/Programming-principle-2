import pygame
import random, time

pygame.init()
running = True
WIDTH, HEIGHT = 1200, 800
FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LEVEL = 0

font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anaconda")
clock = pygame.time.Clock()

# Handler
def handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

# Checking collisions between snake and walls
def check_collision(x,y):
    global running
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 40:
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (550,400))
        scoretag = font.render("Your score: "+str(s.score), True, BLACK)
        screen.blit(scoretag, (550,500))

        pygame.display.update()

        time.sleep(2)
        
        pygame.quit()

# Snake object 
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 600
        self.y = 400
        self.dx = 3
        self.dy = 3
        self.score = 0
        self.i = 5 # Speed increment
        self.direction = "RIGHT" # Base directon
        self.directionsnake = {"LEFT" : False, "RIGHT" : True, "UP" : True, "DOWN" : True}
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.segments = [(self.x, self.y)]    
    # Keyboard pressed
    def press(self):
        pressed_keys = pygame.key.get_pressed()
        directions = {pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT', pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN'}
        for key, direction in directions.items():
            if pressed_keys[key]:
                if direction == "LEFT" and self.directionsnake["LEFT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : True, "RIGHT" : False, "UP" : True, "DOWN" : True}
                elif direction == "RIGHT" and self.directionsnake["RIGHT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : False, "RIGHT" : True, "UP" : True, "DOWN" : True}
                elif direction == "UP" and self.directionsnake["UP"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : True, "RIGHT" : True, "UP" : True, "DOWN" : False}
                elif direction == "DOWN" and self.directionsnake["DOWN"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT" : True, "RIGHT" : True, "UP" : False, "DOWN" : True}

    def move(self):
        global LEVEL
        head_x, head_y = self.segments[0]
        if self.direction == 'LEFT':
            head_x -= self.dx
        elif self.direction == 'RIGHT':
            head_x += self.dx
        elif self.direction == 'UP':
            head_y -= self.dy
        elif self.direction == 'DOWN':
            head_y += self.dy
        self.rect = pygame.Rect(head_x, head_y, 10,10)
        self.segments.insert(0, (head_x, head_y))

        if not pygame.sprite.spritecollide(self, fruits, False):
            self.segments.pop()
        else:
            self.score += 1
            if s.score % self.i == 0: # Upgrading level
                s.dx += 0.4
                s.dy += 0.4
                self.i += 10
                LEVEL += 1

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, RED, (segment[0], segment[1], 10, 10))

# Fruits object
class Fruits(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randrange(10, 1190, 50)
        self.y = random.randrange(40, 790, 50)
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
    def born(self):
        pygame.draw.rect(screen, BLUE, self.rect)


s = Snake()
f = Fruits()
fruits = pygame.sprite.Group()
fruits.add(f)

# Game cycle
while running:
    clock.tick(FPS)
    running = handler()
    screen.fill(BLACK)
    pygame.draw.aaline(screen, BLUE, [0, 40], [1200, 40])
    
    scoretag = font.render("Score: "+str(s.score), True, (0, 255, 0))
    leveltag = font.render("Level: "+str(LEVEL), True, (0, 255, 0))
    screen.blit(scoretag, (10,10))
    screen.blit(leveltag, (1100, 10))

    

    for entity in fruits:
        entity.born()

    s.press()
    s.move()

    if pygame.sprite.spritecollide(s, fruits, True):
        f = Fruits()
        fruits.add(f)

    s.draw()

    

    check_collision(s.segments[0][0], s.segments[0][1])

    pygame.display.update()




pygame.quit()
