import pygame
from pygame.locals import *
import time
import random

pygame.init()
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Mouse And Cheese Game")

SIZE = 40
BACKGROUND_COLOR = (0, 80, 50)

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("data/mouse.png").convert()
        self.x = [40]
        self.y = [40]
        self.length = 1
        self.direction = 'down'

    def move_left(self): self.direction = 'left'
    def move_right(self): self.direction = 'right'
    def move_up(self): self.direction = 'up'
    def move_down(self): self.direction = 'down'

    def walk(self):
        # move tail
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # move head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("data/cheese.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

def is_collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + SIZE:
        if y1 >= y2 and y1 < y2 + SIZE:
            return True
    return False

def display_score(surface, score):
    font = pygame.font.SysFont('arial', 30)
    score_text = font.render(f"Score: {score}", True, (200, 200, 200))
    surface.blit(score_text, (850, 10))

def game_over(surface, score):
    font = pygame.font.SysFont('arial', 60)
    text = font.render(f"Game Over! Your Score: {score}", True, (255, 0, 0))
    surface.blit(text, (400, 400))
    pygame.display.flip()
    time.sleep(3)

snake = Snake(screen)
apple = Apple(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                snake.move_left()
            if event.key == K_RIGHT:
                snake.move_right()
            if event.key == K_UP:
                snake.move_up()
            if event.key == K_DOWN:
                snake.move_down()

    snake.walk()
    apple.draw()
    display_score(screen, snake.length)

    # Check collision with apple
    if is_collision(snake.x[0], snake.y[0], apple.x, apple.y):
        snake.increase_length()
        apple.move()

    # Check collision with itself
    for i in range(1, snake.length):
        if is_collision(snake.x[0], snake.y[0], snake.x[i], snake.y[i]):
            game_over(screen, snake.length)
            running = False
            break

    time.sleep(0.25)
