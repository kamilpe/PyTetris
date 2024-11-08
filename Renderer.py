import pygame
from config import *

def draw_bricks(surface, x, y, bricks_map):
    cur_y = y
    for row in bricks_map:
        cur_x = x
        for brick in row:
            if brick:
                surface.fill(BLOCK_COLOR, (cur_x, cur_y, BRICK_SIZE, BRICK_SIZE))
            cur_x+=BRICK_SIZE
        cur_y+=BRICK_SIZE

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.points_font = pygame.font.SysFont("Sans", POINTS_FONT_SIZE)
        self.info_font = pygame.font.SysFont("Sans", INFO_FONT_SIZE)

    def draw_interface(self, tetris_board):
        self.screen.fill(BG_COLOR)

        # Main plate:
        # outer shadow
        pygame.draw.rect(self.screen, FRAME_OUTER_SHADOW, (
            BOARD_POS_X, 
            BOARD_POS_Y, 
            BOARD_SIZE_W+2,
            BOARD_SIZE_H+2), 1)
        # border
        pygame.draw.rect(self.screen, FRAME_BORDER, (
            BOARD_POS_X-1, 
            BOARD_POS_Y-1, 
            BOARD_SIZE_W+2,
            BOARD_SIZE_H+2), 1)

        # Next pattern plate:        
        # outer shadow
        pygame.draw.rect(self.screen, FRAME_OUTER_SHADOW, (
            BOARD_POS_X + BOARD_SIZE_W + 50, 
            BOARD_POS_Y, 
            BRICK_SIZE*6 + 2,
            BRICK_SIZE*6 + 2), 1)
        # border
        pygame.draw.rect(self.screen, FRAME_BORDER, (
            BOARD_POS_X + BOARD_SIZE_W + 49, 
            BOARD_POS_Y-1, 
            BRICK_SIZE*6 + 2,
            BRICK_SIZE*6 + 2), 1)

        info1 = self.info_font.render("Press R to reset the game", True, INFO_COLOR)
        self.screen.blit(info1, (INFO_POS_X, INFO_POS_Y))
        info2 = self.info_font.render("Press Q or EXC to exit", True, INFO_COLOR)
        self.screen.blit(info2, (INFO_POS_X, INFO_POS_Y + info1.get_height()))

    def draw_game(self, tetris_board):
        # Points:
        points = self.points_font.render("Points: " + str(tetris_board.points), True, POINTS_COLOR)
        self.screen.fill(BG_COLOR, (POINTS_POS_X, 
                                    POINTS_POS_Y,
                                    points.get_width(),
                                    points.get_height()))
        self.screen.blit(points, (POINTS_POS_X, POINTS_POS_Y))
    
        # Board
        pygame.draw.rect(self.screen, FRAME_INNER, (
            BOARD_POS_X, 
            BOARD_POS_Y, 
            BOARD_SIZE_W, 
            BOARD_SIZE_H))

        # Next brick window
        pygame.draw.rect(self.screen, FRAME_INNER, (
            BOARD_POS_X + BOARD_SIZE_W + 50, 
            BOARD_POS_Y, 
            BRICK_SIZE*6, 
            BRICK_SIZE*6))

        # draw bricks
        draw_bricks(self.screen, BOARD_POS_X, BOARD_POS_Y, tetris_board.board)

        # draw current block
        draw_bricks(self.screen, 
                    BOARD_POS_X + tetris_board.current_block_x * BRICK_SIZE,
                    BOARD_POS_Y + tetris_board.current_block_y * BRICK_SIZE,
                    tetris_board.current_block)

        # draw next block
        draw_bricks(self.screen, 
                    BOARD_POS_X + BOARD_SIZE_W + 50 + BRICK_SIZE,
                    BOARD_POS_Y + BRICK_SIZE,
                    tetris_board.next_block)
        
        pygame.display.flip()


    