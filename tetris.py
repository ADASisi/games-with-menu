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
    def __init__ (self, colume, row, shape):
        self.x = colume
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_position = {}):
    grid = [[(0, 0, 0) for x in range(10)] for y in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_position:
                    c = locked_position[(j, i)]
                    grid[i][j] = c
    
    return grid

def convert_shape_format(current_shape):
    positions = []

    shape_format = current_shape.shape[current_shape.rotation  % len(current_shape.shape)] #?

    for i, line in enumerate (shape_format):
        row = list(line)
        for j, colume in enumerate(row):
            if colume == '0':
                positions.append((current_shape.x + j, current_shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

def get_shape():
    return  Piece(5, 0, random.choice(shapes))

def valid_space(shape, grid):
    accepted_position = [[(j, i) for j in range (10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_position = [j for sub in accepted_position for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_position:
            if pos[1] > -1:
                return False

    return True

def check_lost(positions):
    pass

def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y
    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size), (sx + play_width, sy + i * block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comiceans', 40)

    label = font.render("Next Shape", 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    shape_format = shape.shape[shape.rotation  % len(shape.shape)] #?

    for i, line in enumerate(shape_format):
        row = list(line)
        for j, colume in enumerate(row):
            if colume == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * block_size, sy + i * block_size, block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy - 30))

def draw_window(surface, grid):

    surface.fill((0,0,0))

    pygame.font.init()

    font = pygame.font.SysFont('Helvetica', 20) 

    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)

    draw_grid(surface, grid)

def main(win):
    run = True
    locked_position = {}

    grid = create_grid(locked_position)

    change_piece = False
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    while run:

        grid = create_grid(locked_position)
        fall_time += clock.get_rawtime() #gives milliseconds
        clock.tick()

        if fall_time/1000 > fall_speed: 
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece,  grid) and current_piece.y > 0 :  
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
    
        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_position[p] = current_piece.color
            next_piece = get_shape()
            current_piece = next_piece
            change_piece = False

        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_position):
            run = False
    
    pygame.display.quit()

def main_menu(win):
    main(win)

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")

main_menu(win)

