import pygame 
from pygame.locals import *
import random, time
import sys

# Settings
pygame.init()
running = True
WIDTH = 400
HEIGHT = 600
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPEED = 5
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()
background = pygame.image.load("images/AnimatedStreet.png")
SCORE = 0
COINS = 0
i = 5
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

def handler(): # Event handler
    global SPEED
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            return False
    return True

class Enemy(pygame.sprite.Sprite):  # Obstacle class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), -10)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 40), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):  # Coin class
    def __init__(self, id, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.identify = id
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 40), 0)
            if pygame.sprite.spritecollideany(self, enemies) or pygame.sprite.spritecollideany(self, coins_s):
                self.rect.center = (random.randint(30, WIDTH - 40), 0)

class Player(pygame.sprite.Sprite): # Player class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Initializing game objects and creating groups
P1 = Player()
E1 = Enemy()
C1 = Coin("Coin1", "images/coin1.png")
C2 = Coin("Coin2", "images/coin2.png")
C3 = Coin("Coin3", "images/coin3.png")
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_s = pygame.sprite.Group()
coins_s.add(C1, C2, C3)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1, C2, C3)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

while running:
    clock.tick(FPS)
    running = handler()

    screen.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coins = font_small.render("Coins: " + str(COINS), True, BLACK)
    screen.blit(scores, (10, 10))
    screen.blit(coins, (300, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
      
        pygame.mixer.Sound('sounds/crash.wav').play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollide(P1, coins_s, False):
        for coin in pygame.sprite.spritecollide(P1, coins_s, False):
            if coin.identify == "Coin1":
                COINS += 1
                coin.kill()
                C1 = Coin("Coin1", "images/coin1.png")
                coins_s.add(C1)
                all_sprites.add(C1)
            elif coin.identify == "Coin2":
                COINS += 2
                coin.kill()
                C2 = Coin("Coin2", "images/coin2.png")
                coins_s.add(C2)
                all_sprites.add(C2)
            elif coin.identify == "Coin3":
                COINS += 3
                coin.kill()
                C3 = Coin("Coin3", "images/coin3.png")
                coins_s.add(C3)
                all_sprites.add(C3)
    if COINS % i == 0 and COINS:
        SPEED += 0.5
        i += 10

    pygame.display.update()

pygame.quit()
sys.exit()
