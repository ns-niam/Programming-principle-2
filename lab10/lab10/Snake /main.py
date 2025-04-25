import pygame
import random
import time
import psycopg2
import sys

# Initialize pygame
pygame.init()

# Connect to PostgreSQL
connection = psycopg2.connect(
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432",
    database="snake"
)

# Fetch or create user info
def get_user_info(connection, username):
    with connection.cursor() as cur:
        cur.execute("SELECT level, score FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result is None:
            cur.execute("INSERT INTO users (username, level, score) VALUES (%s, 0, 0)", (username,))
            connection.commit()
            return {"level": 0, "score": 0}
        else:
            return {"level": result[0], "score": result[1]}

# Update user score and level
def set_new_score(connection, username, score, level):
    with connection.cursor() as cur:
        cur.execute("UPDATE users SET score = %s, level = %s WHERE username = %s", (score, level, username))
        connection.commit()

# Game setup
WIDTH, HEIGHT = 1200, 800
FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

LEVEL = 0

# Username input
username = input("What is your name: ")
user_info = get_user_info(connection, username)

HIGHLEVEL = user_info["level"]
HIGHSCORE = user_info["score"]

font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Event handler
def handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            set_new_score(connection, username, s.score, LEVEL)
            pygame.quit()
            sys.exit()
    return True

# End game if hitting wall
def check_collision(x, y):
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 40:
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (550, 400))
        scoretag = font.render("Your score: " + str(s.score), True, BLACK)
        screen.blit(scoretag, (550, 500))
        set_new_score(connection, username, s.score, LEVEL)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

# Snake class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 600
        self.y = 400
        self.dx = 3
        self.dy = 3
        self.score = 0
        self.i = 5
        self.direction = "RIGHT"
        self.directionsnake = {"LEFT": False, "RIGHT": True, "UP": True, "DOWN": True}
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.segments = [(self.x, self.y)]

    def press(self):
        pressed_keys = pygame.key.get_pressed()
        directions = {pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT', pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN'}
        for key, direction in directions.items():
            if pressed_keys[key]:
                if direction == "LEFT" and self.directionsnake["LEFT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": True, "RIGHT": False, "UP": True, "DOWN": True}
                elif direction == "RIGHT" and self.directionsnake["RIGHT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": False, "RIGHT": True, "UP": True, "DOWN": True}
                elif direction == "UP" and self.directionsnake["UP"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": True, "RIGHT": True, "UP": True, "DOWN": False}
                elif direction == "DOWN" and self.directionsnake["DOWN"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": True, "RIGHT": True, "UP": False, "DOWN": True}

    def move(self, add=1, start=0):
        global LEVEL
        head_x, head_y = self.segments[0]
        if self.direction == 'LEFT':
            head_x -= self.dx * add
        elif self.direction == 'RIGHT':
            head_x += self.dx * add
        elif self.direction == 'UP':
            head_y -= self.dy * add
        elif self.direction == 'DOWN':
            head_y += self.dy * add
        self.rect = pygame.Rect(head_x, head_y, 10, 10)
        self.segments.insert(0, (head_x, head_y))

        if not pygame.sprite.spritecollide(self, fruits, False):
            self.segments.pop()
        else:
            self.score += add * start
            if self.score % self.i == 0:
                self.dx += 0.4
                self.dy += 0.4
                self.i += 10
                LEVEL += 1

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, RED, (segment[0], segment[1], 10, 10))

# Fruits class
class Fruits(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__()
        self.x = random.randrange(10, 1190, 50)
        self.y = random.randrange(40, 790, 50)
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.identify = id
        self.created_time = time.time()

    def born(self):
        if self.identify == 1:
            pygame.draw.rect(screen, BLUE, self.rect)
        elif self.identify == 2:
            pygame.draw.rect(screen, "green", self.rect)
        elif self.identify == 3:
            pygame.draw.rect(screen, "gold", self.rect)
        elif self.identify == 4:
            pygame.draw.rect(screen, "white", self.rect)

# Create snake and fruits
s = Snake()
f1 = Fruits(1)
f2 = Fruits(2)
f3 = Fruits(3)
f4 = Fruits(4)
fruits = pygame.sprite.Group()
fruits.add(f1, f2, f3, f4)

# Pause function
def pause_game():
    paused = True
    pause_text = font.render("Game Paused - Press 'P' to resume", True, (255, 255, 255))
    screen.blit(pause_text, (400, 400))
    pygame.display.update()
    set_new_score(connection, username, s.score, LEVEL)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False
        clock.tick(5)

# Draw walls based on level
def draw_wall(level):
    if level >= 1:
        pygame.draw.rect(screen, (200, 200, 200), (300, 200, 600, 20))
    if level >= 2:
        pygame.draw.rect(screen, (200, 200, 200), (500, 200, 20, 400))

# Main game loop
running = True
while running:
    clock.tick(FPS)
    running = handler()
    screen.fill(BLACK)

    pygame.draw.aaline(screen, BLUE, [0, 40], [1200, 40])

    scoretag = font.render("Score: " + str(s.score), True, (0, 255, 0))
    leveltag = font.render("Level: " + str(LEVEL), True, (0, 255, 0))
    highscoretag = font.render("High Score: " + str(HIGHSCORE), True, (0, 255, 0))
    highleveltag = font.render("High Level: " + str(HIGHLEVEL), True, (0, 255, 0))

    screen.blit(scoretag, (10, 10))
    screen.blit(leveltag, (1100, 10))
    screen.blit(highscoretag, (110, 10))
    screen.blit(highleveltag, (900, 10))

    for entity in fruits:
        entity.born()

    s.press()
    s.move()

    if time.time() - f4.created_time >= 5:
        f4.kill()
        f4 = Fruits(4)
        fruits.add(f4)

    if pygame.sprite.spritecollide(s, fruits, False):
        for fruct in pygame.sprite.spritecollide(s, fruits, False):
            if fruct.identify == 1:
                s.move(1, 1)
                f1.kill()
                f1 = Fruits(1)
                fruits.add(f1)
            elif fruct.identify == 2:
                s.move(2, 1)
                f2.kill()
                f2 = Fruits(2)
                fruits.add(f2)
            elif fruct.identify == 3:
                s.move(3, 1)
                f3.kill()
                f3 = Fruits(3)
                fruits.add(f3)
            elif fruct.identify == 4:
                s.move(5, 1)
                f4.kill()
                f4 = Fruits(4)
                fruits.add(f4)

    s.draw()
    check_collision(s.segments[0][0], s.segments[0][1])
    draw_wall(LEVEL)

    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        pause_game()

pygame.quit()
sys.exit()
