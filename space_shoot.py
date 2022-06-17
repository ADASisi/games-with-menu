import pygame
import os
pygame.font.init()


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shoot")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUЕ = (0, 0, 255)

BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)


FPS = 60
VELOSITY = 3
BULLET_VEL = 10
MAX_BULLETS = 5
SPACESHIP_WIDTH, SPACE_HEIGHT = 55, 40

BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BLUE_SPACESHIP_IMAGE = pygame.image.load(os.path.join('spaceship_blue.png'))
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
BLUE_SPACESHIP_IMAGE, (50, 40)), 270)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACE_HEIGHT)), 90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('space.png')), (WIDTH, HEIGHT))


def draw_window(red, blue, red_bullets, blue_bullets, red_health, blue_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    blue_health_text = HEALTH_FONT.render("Health: " + str(blue_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(blue_health_text, (10, 10))

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
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            blue_bullets.remove(bullet)
            
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
     
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    
    
def main():
    red = pygame.Rect(650, 220, SPACESHIP_WIDTH, SPACE_HEIGHT)
    blue = pygame.Rect(200, 220, SPACESHIP_WIDTH, SPACE_HEIGHT)
    
    red_bullets = []
    blue_bullets = []
    
    red_health = 10
    blue_health = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:      
        clock.tick(FPS)  
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(blue_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(blue.x + blue.width, blue.y + blue.height/2 - 2, 10, 5)
                    blue_bullets.append(bullet)
                    
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x + red.height, red.y + red.height/2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    
            if event.type == RED_HIT:
                red_health -= 1
                
            if event.type == BLUE_HIT:
                blue_health -= 1
              
        winner_text = ""
        if red_health <= 0:
            winner_text = "Blue wins!!!"
            
        if blue_health <= 0:
            winner_text = "Red wins!!!"
          
        if winner_text != "":
            draw_winner(winner_text)
            break
        
        key_pressed = pygame.key.get_pressed()
        blue_ship_movement(key_pressed, blue)
        red_ship_movement(key_pressed, red)     
        
        handle_bullets(blue_bullets, red_bullets, blue, red)
           
        draw_window(red, blue, red_bullets, blue_bullets, red_health, blue_health)    
        
main()

    
    
    
if __name__ == "__main__":
    main()