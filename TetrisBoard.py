import random
import pygame
from config import *

PATTERNS = [
            [[1,1],
            [2,1]],

            [[1,2,1,1]],

            [[0,0,1],
             [1,2,1]],

            [[0,1,1],
             [1,2,0]],

            [[0,1,0],
             [1,2,1]]]

def rotate_matrix(matrix):
    new_matrix = []
    w = len(matrix[0])
    h = len(matrix)
    return new_matrix

class TetrisBoard:       
    def __init__(self):     
        self.board = [
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
        random.seed(pygame.time.get_ticks())
    
    def inject(self, block):
        self.current_block = block
        block_width = len(self.current_block)
        self.current_block_x = int(BOARD_BLOCKS_W / 2 - block_width / 2)
        self.current_block_y = 0
        self.turn_block(1)

    def get_block(self,index, mirror=False):
        print('Creating',index,'mirror:',mirror)
        return PATTERNS[index]

    def get_random_block(self):
        return self.get_block(random.randint(0, len(PATTERNS)-1),
                              random.randint(0, 1))

    def turn_block(self, val):
        row_idx = 0
        brick_idx = 0
        for row in self.current_block:
            brick_idx = 0
            for brick in row:
                if brick:
                    y = self.current_block_y + row_idx
                    x = self.current_block_x + brick_idx
                    self.board[y][x] = val
                brick_idx+=1
            row_idx+=1

    def advance(self):
        if self.current_block_y + len(self.current_block) + 1 > BOARD_BLOCKS_H:
            self.inject(self.get_random_block())
            return
        self.turn_block(0)
        self.current_block_y+=1
        self.turn_block(1)
    
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
