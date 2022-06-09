import pygame
import random
"""0 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
""" 
pygame.font.init()
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300 
# meaning 300 // 10 = 30 width per block
play_height = 600 
# meaning 600 // 20 = 20 height per block
block_size = 30
top_left_x = (s_width - play_width) // 2

top_left_y = s_height - play_height

S = [[
'.....',
'.....',
'..00.',
'.00..',
'.....'],
['.....',
'..0..',
'..00.',
'...0.',
'.....']]

Z = [[
'.....',
'.....',
'.00..',
'..00.',
'.....'],
['.....',
'..0..',
'.00..',
'.0...',
'.....']]

I = [[
'..0.',
'..0..',
'..0..',
'..0..',
'.....'],
['.....',
'0000.',
'.....',
'.....',
'.....']]

O = [[
'.....',
'.....',
'.00..',
'.00..',
'.....']]

J = [[
'.....',
'.0...',
'.000.',
'.....',
'.....'],
['.....',
'..00.',
'..0..',
'..0..',
'.....'],
['.....',
'.....',
'.000.',
'...0.',
'.....'],
['.....',
'..0..',
'..0..',
'.00..',
'.....']]

L = [[
'.....',
'...0.',
'.000.',
'.....',
'.....'],
['.....',
'..0..',
'..0..',
'..00.',
'.....'],
['.....',
'.....',
'.000.',
'.0...',
'.....'],
['.....',
'.00..',
'..0..',
'..0..',
'.....']]

T = [[
'.....',
'..0..',
'.000.',
'.....',
'.....'],
['.....',
'..0..',
'..00.',
'..0..',
'.....'],
['.....',
'.....',
'.000.',
'..0..',
'.....'],
['.....',
'..0..',
'.00..',
'..0..',
'.....']]

shapes = [S, Z, I, O, J, L, T]

shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165 ,0), (0,0,255), (128, 0, 128)]

class Piece(object):
    def _init_ (self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_position = {}):
    grid = [[(0, 0, 0)     for x in range(10)] for y in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_position:
                    c = locked_position[(j, i)]
                    grid[i][j] = c
    
    return grid

def get_shape():
    return  Piece(5, 0, random.choice(shapes))

def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y
    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size), (sx + play_width, sy + i * block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))


def draw_window(surface, grid):

    surface.fill(0,0,0)

    pygame.font.init()

    font = pygame.font.SysFont('Helvetica', 20) 

    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, ((top_left_x + play_width) / 2 - (label.get_width/2), 30))


    for i in range(len(grid)):
        for j in range(grid[i]):
            pygame.draw.rect(surface, grid[i][j], top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size, 0)

    pygame.draw.rect(surface, (255, 0, 0), top_left_x, top_left_y, play_width, play_height, 4)

    draw_grid(surface, grid)
    
    pygame.display.update()



def main(win):
    run = True
    locked_position = {}

    grid = create_grid(locked_position)

    change_piece = False
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_RIGHT:
                    if valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_UP:
                    if valid_space(current_piece, grid):
                        current_piece.rotation += 1
                if event.key == pygame.K_DOWN:
                    if valid_space(current_piece, grid):    
                        current_piece.y += 1
    
    draw_window(win, grid)


def main_menu(win):
    main(win)

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")

main_menu(win)

