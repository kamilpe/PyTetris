import random
import pygame
from config import *

PATTERNS = [
            [[1,1],
            [2,1]],

            [[1],
             [1],
             [2],
             [1]],

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
    NO_ACTION = 0
    ACTION_IMPACT = 1

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
        self.next_block = self.get_random_block()
        random.seed(pygame.time.get_ticks())
    
    def inject(self, block):
        self.current_block = block
        block_width = len(self.current_block)
        self.current_block_x = int(BOARD_BLOCKS_W / 2 - block_width / 2)
        self.current_block_y = 0


    def get_block(self,index, mirror=False):
        print('Creating',index,'mirror:',mirror)
        return PATTERNS[index]

    def get_random_block(self):
        return self.get_block(random.randint(0, len(PATTERNS)-1),
                              random.randint(0, 1))

    def advance(self):
        if self.simulate_action(self.current_block_x, self.current_block_y) == self.ACTION_IMPACT:
            self.burn_current_block()
            self.inject(self.next_block)
            self.next_block = self.get_random_block()
            return
        self.current_block_y+=1

    def simulate_action(self, next_x, next_y):
        next_row = next_y + len(self.current_block)
        if next_row >= BOARD_BLOCKS_H:
            return self.ACTION_IMPACT
            
        row_idx = 0
        brick_idx = 0
        for row in self.current_block:
            brick_idx = 0
            for brick in row:
                if brick:
                    y = self.current_block_y + row_idx + 1
                    x = self.current_block_x + brick_idx
                    if self.board[y][x]:
                        return self.ACTION_IMPACT
                brick_idx+=1
            row_idx+=1        

        return self.NO_ACTION
    
    def burn_current_block(self):
        row_idx = 0
        brick_idx = 0
        for row in self.current_block:
            brick_idx = 0
            for brick in row:
                if brick:
                    y = self.current_block_y + row_idx
                    x = self.current_block_x + brick_idx
                    self.board[y][x] = 1
                brick_idx+=1
            row_idx+=1
    
    def left(self):
        if self.current_block_x > 0:
            self.current_block_x-=1
    
    def right(self):
        if self.current_block_x + len(self.current_block[0]) < BOARD_BLOCKS_W:
            self.current_block_x+=1

    def rotate(self):
        self.current_block = rotate_matrix(self.current_block)
