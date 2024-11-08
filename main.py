import pygame
import random

BLOCK_SIZE = 9
BOARD_BLOCKS_W = 10
BOARD_BLOCKS_H = 20
BOARD_SIZE_W = BOARD_BLOCKS_W * BLOCK_SIZE
BOARD_SIZE_H = BOARD_BLOCKS_H * BLOCK_SIZE
BOARD_POS_X = 10
BOARD_POS_Y = 10

def rotate_matrix(matrix):
    new_matrix = []
    w = len(matrix[0])
    h = len(matrix)

    return new_matrix

class TetrisBoard:  
    block = [[[1,1],
              [2,1]],

             [[1,2,1,1]],

             [[0,0,1],
              [1,2,1]],

             [[0,1,1],
              [1,2,0]]]
        
    def __init__(self):     
        self.board_map = [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]
        self.current_block = []
        self.current_block_x = 0
        self.current_block_y = 0
        self.inject(self.get_random_block())
    
    def inject(self, block):
        self.current_block = block
        block_width = len(self.current_block)
        self.current_block_x = int(BOARD_BLOCKS_W / 2 - block_width / 2)
        self.current_block_y = 0
        self.turn_block(1)

    def turn_block(self, val):
        row_idx = 0
        brick_idx = 0
        for row in self.current_block:
            brick_idx = 0
            for brick in row:
                if brick:
                    y = self.current_block_y + row_idx
                    x = self.current_block_x + brick_idx
                    self.board_map[y][x] = val
                brick_idx+=1
            row_idx+=1

    def advance(self):
        if self.current_block_y + len(self.current_block) + 1 > BOARD_BLOCKS_H:
            self.inject(self.get_random_block())
            return
        self.turn_block(0)
        self.current_block_y+=1
        self.turn_block(1)
        

    def get_block(self,index, mirror=False):
        print('Creating',index,'mirror:',mirror)
        return self.block[index]

    def get_random_block(self):
        random.seed(pygame.time.get_ticks())
        return self.get_block(random.randint(0, len(self.block)-1),
                              random.randint(0, 1))
    
    def left(self):
        if self.current_block_x > 0:
            self.turn_block(0)
            self.current_block_x-=1
            self.turn_block(1)
    
    def right(self):
        if self.current_block_x + len(self.current_block[0]) < BOARD_BLOCKS_W:
            self.turn_block(0)
            self.current_block_x+=1
            self.turn_block(1)

    def rotate(self):
        self.current_block = rotate_matrix(self.current_block)

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_interface(self, game_data):
        screen.fill("darkcyan")
        # Outer shadow
        pygame.draw.rect(screen, "grey1", (BOARD_POS_X, BOARD_POS_Y, BOARD_SIZE_W+2,BOARD_SIZE_H+2), 1)
        # Border
        pygame.draw.rect(screen, "blue", (BOARD_POS_X-1, BOARD_POS_Y-1, BOARD_SIZE_W+2,BOARD_SIZE_H+2), 1)

        info = info_font.render("Next:", False, "dark blue")
        screen.blit(info, (BOARD_POS_X + BOARD_SIZE_W + 20, BOARD_POS_Y))

        # Outer shadow
        pygame.draw.rect(screen, "grey1", (BOARD_POS_X + BOARD_SIZE_W + 50, 
                                       BOARD_POS_Y, 
                                       BLOCK_SIZE*4 +2,
                                       BLOCK_SIZE*4 +2), 1)
        # Border
        pygame.draw.rect(screen, "blue", (BOARD_POS_X + BOARD_SIZE_W + 49, 
                                          BOARD_POS_Y-1, 
                                          BLOCK_SIZE*4 +2,
                                          BLOCK_SIZE*4 +2), 1)

        points = points_font.render("Points: 35", False, "dark blue")
        screen.blit(points, (160,90))

        info = info_font.render("Press R to reset the game", False, "green")
        screen.blit(info, (150,170))
        info = info_font.render("Press Q or EXC to exit", False, "green")
        screen.blit(info, (150,180))

    def draw_game(self, game_data):
        # Board
        pygame.draw.rect(screen, "grey50", (BOARD_POS_X, BOARD_POS_Y, BOARD_SIZE_W, BOARD_SIZE_H))

        # Next brick window
        pygame.draw.rect(screen, "grey50", (BOARD_POS_X + BOARD_SIZE_W + 50, 
                                        BOARD_POS_Y, 
                                        BLOCK_SIZE*4, 
                                        BLOCK_SIZE*4))

        # draw bricks
        cur_y = BOARD_POS_Y
        for row in game_data.board_map:
            cur_x = BOARD_POS_X
            for brick in row:
                if brick:
                    screen.fill("dark red", (cur_x, cur_y, BLOCK_SIZE, BLOCK_SIZE))
                cur_x+=BLOCK_SIZE
            cur_y+=BLOCK_SIZE

        pygame.display.flip()

class GameControl:
    def __init__(self, board, renderer):
        self.board = board
        self.renderer = renderer
        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()        
        self.current_delay = 750
        self.target_delay = 750
        self.running = True

    def game_loop(self):
        self.renderer.draw_interface(self.board)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]: 
                        self.board.left()
                    if keys[pygame.K_RIGHT]:
                        self.board.right()
                    if keys[pygame.K_DOWN]:
                        self.current_delay = 50
                    if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                        self.running = False
                if event.type == pygame.KEYUP:
                    keys = pygame.key.get_pressed()
                    if not keys[pygame.K_DOWN]:
                        self.current_delay = self.target_delay

            next_update = self.last_tick + self.current_delay
            if pygame.time.get_ticks() >= next_update:
                self.last_tick = pygame.time.get_ticks()
                self.board.advance()

            self.renderer.draw_game(self.board)
            self.clock.tick(60)
            

pygame.init()
pygame.font.init()
points_font = pygame.font.SysFont("Fixed bold", 28)
info_font = pygame.font.SysFont("Sans", 10)
screen = pygame.display.set_mode((320,200),pygame.RESIZABLE | pygame.SCALED)

game = GameControl(TetrisBoard(), Renderer(screen))
game.game_loop()

pygame.quit()