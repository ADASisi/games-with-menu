import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.png").convert()
        self.block = pygame.transform.scale(self.block, (40, 40))
        self.block_x = 100
        self.block_y = 100
        self.direction = 'down'
    def draw(self):
        self.parent_screen.fill((0, 0, 0))
        self.parent_screen.blit(self.block, (self.block_x, self.block_y))
        pygame.display.flip()
    def move_up(self):
        self.block_y -= 10
        self.draw()
    def move_down(self):
        self.block_y += 10
        self.draw()
    def move_left(self):
        self.block_x -= 10
        self.draw()
    def move_right(self):
        self.block_x += 10
        self.draw()
    def walk(self):
        if self.direction == 'up':
            self.block_y -= 10
        if self.direction == 'down':
            self.block_y += 10
        if self.direction == 'left':
            self.block_x -= 10
        if self.direction == 'right':
            self.block_x += 10
        self.draw()

        
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.window.fill((0, 0, 0))
        self.snake = Snake(self.window)
        self.snake.draw()
    def run(self):
        running = True

        while running: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
            self.snake.walk()
            time.sleep(0.2)
                



    
# --------------------------------------------------------------------------
game = Game()
game.run()