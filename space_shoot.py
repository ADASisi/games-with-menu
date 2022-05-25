from tkinter import EventType
import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shoot")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUЕ = (0, 0, 255)

BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT)

FPS = 60
VELOSITY = 3
BULLET_VEL = 7
MAX_BULLETS = 5
SPACESHIP_WIDTH, SPACE_HEIGHT = 55, 40

BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BLUE_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('spaceship_blue.png'))
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    BLUE_SPACESHIP_IMAGE, (50, 40)), 270)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACE_HEIGHT)), 90)


def draw_window(red, blue, red_bullets, blue_bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(BLUE_SPACESHIP, (blue.x, blue.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in blue_bullets:
        pygame.draw.rect(WIN, BLUЕ, bullet)
    
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
    if key_pressed[pygame.K_LEFT] and red.x - VELOSITY > BORDER.x + BORDER.width:
            red.x -= VELOSITY
    if key_pressed[pygame.K_RIGHT] and red.x + VELOSITY + red.width < WIDTH:
            red.x += VELOSITY
    if key_pressed[pygame.K_UP] and red.y - VELOSITY > 0:
            red.y -= VELOSITY
    if key_pressed[pygame.K_DOWN] and red.y + VELOSITY + red.height < HEIGHT -20 :
            red.y += VELOSITY
            
def handle_bullets(blue_bullets, red_bullets, blue, red):
    for bullet in blue_bullets:
        bullet.x += BULLET_VEL
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)
            
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
               
def main():
    red = pygame.Rect(650, 220, SPACESHIP_WIDTH, SPACE_HEIGHT)
    blue = pygame.Rect(200, 220, SPACESHIP_WIDTH, SPACE_HEIGHT)
    
    red_bullets = []
    blue_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:      
        clock.tick(FPS)  
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(blue_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(blue.x + blue.width, blue.y + blue.height/2 - 2, 10, 5)
                blue_bullets.append(bullet)
                    
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x + red.height, red.y + red.height/2 - 2, 10, 5)
                red_bullets.append(bullet)
        key_pressed = pygame.key.get_pressed()
        blue_ship_movement(key_pressed, blue)
        red_ship_movement(key_pressed, red)     
        
        handle_bullets(blue_bullets, red_bullets, blue, red)
           
        draw_window(red, blue, red_bullets, blue_bullets)    
        
    pygame.quit()

    
if __name__ == "__main__":
    main()