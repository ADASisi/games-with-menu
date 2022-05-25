from tkinter import EventType
import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN  =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shoot")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT)

FPS = 60
VELOSITY = 3
SPACESHIP_WIDTH, SPACE_HEIGHT = 55, 40

BLUE_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('spaceship_blue.png'))
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    BLUE_SPACESHIP_IMAGE, (50, 40)), 270)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACE_HEIGHT)), 90)


def draw_window(red, blue):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(BLUE_SPACESHIP, (blue.x, blue.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

  
def blue_ship_movement(key_pressed, blue):
    if key_pressed[pygame.K_a] and blue.x - blue.height > 0:
            blue.x -= VELOSITY
    if key_pressed[pygame.K_d] and blue.x + VELOSITY + blue.width < BORDER.x:
            blue.x += VELOSITY
    if key_pressed[pygame.K_w] and blue.y - VELOSITY > 0:
            blue.y -= VELOSITY
    if key_pressed[pygame.K_s] and blue.y + VELOSITY + blue.height < HEIGHT-15:
            blue.y += VELOSITY
            
def red_ship_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x - VELOSITY > 0:
            red.x -= VELOSITY
    if key_pressed[pygame.K_RIGHT] and red.x + VELOSITY + red.width < BORDER.x:
            red.x += VELOSITY
    if key_pressed[pygame.K_UP] and red.y - VELOSITY > 0:
            red.y -= VELOSITY
    if key_pressed[pygame.K_DOWN] and red.y + VELOSITY + red.height < HEIGHT -20 :
            red.y += VELOSITY
        
def main():
    red = pygame.Rect(650, 220, SPACESHIP_WIDTH, SPACE_HEIGHT)
    blue = pygame.Rect(200, 220, SPACESHIP_WIDTH, SPACE_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:      
        clock.tick(FPS)  
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                
        key_pressed = pygame.key.get_pressed()
        blue_ship_movement(key_pressed, blue)
        red_ship_movement(key_pressed, red)

        
        draw_window(red, blue)    
        
    pygame.quit()

    
if __name__ == "__main__":
    main()