import pygame
from config import *

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
            BLOCK_SIZE*4 +2,
            BLOCK_SIZE*4 +2), 1)
        # border
        pygame.draw.rect(self.screen, FRAME_BORDER, (
            BOARD_POS_X + BOARD_SIZE_W + 49, 
            BOARD_POS_Y-1, 
            BLOCK_SIZE*4 +2,
            BLOCK_SIZE*4 +2), 1)

        info1 = self.info_font.render("Press R to reset the game", True, INFO_COLOR)
        self.screen.blit(info1, (INFO_POS_X, INFO_POS_Y))
        info2 = self.info_font.render("Press Q or EXC to exit", True, INFO_COLOR)
        self.screen.blit(info2, (INFO_POS_X, INFO_POS_Y + info1.get_height()))

    def draw_game(self, tetris_board):
        # Points:
        points = self.points_font.render("Points: 35", True, POINTS_COLOR)
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
            BLOCK_SIZE*4, 
            BLOCK_SIZE*4))

        # draw bricks
        cur_y = BOARD_POS_Y
        for row in tetris_board.board:
            cur_x = BOARD_POS_X
            for brick in row:
                if brick:
                    self.screen.fill(BLOCK_COLOR, (cur_x, cur_y, BLOCK_SIZE, BLOCK_SIZE))
                cur_x+=BLOCK_SIZE
            cur_y+=BLOCK_SIZE

        pygame.display.flip()
    