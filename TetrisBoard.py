import random
import pygame
from config import *

PATTERNS = [
            [[0,0,0,0],
             [0,1,1,0],
             [0,1,1,0],
             [0,0,0,0]],

            [[0,0,1,0],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,1,0]],

            [[0,0,0,0],
             [0,0,1,0],
             [0,1,1,1],
             [0,0,0,0]],

            [[0,0,0,0],
             [0,0,1,1],
             [0,1,1,0],
             [0,0,0,0]],

            [[0,0,1,0],
             [0,0,1,0],
             [0,1,1,0],
             [0,0,0,0]]
           ]

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
        self.points = 0
        random.seed(pygame.time.get_ticks())
        self.inject(self.get_random_block())
        self.next_block = self.next_block = self.get_random_block()
    
    def inject(self, block):
        random.seed(pygame.time.get_ticks())
        self.current_block = block
        block_width = len(self.current_block)
        self.current_block_x = int(BOARD_BLOCKS_W / 2 - block_width / 2)
        self.current_block_y = 0

    def get_block(self,index, mirror=False):
        return PATTERNS[index]

    def get_random_block(self):
        return self.get_block(random.randint(0, len(PATTERNS)-1),
                              random.randint(0, 1))

    def advance(self):
        if (self.simulate_action(
            self.current_block_x, 
            self.current_block_y, 
            self.current_block) == self.ACTION_IMPACT):

            self.burnin_current_block()
            self.inject(self.next_block)
            self.next_block = self.get_random_block()
            self.validate_rows()
            return
        self.current_block_y+=1

    def simulate_action(self, next_x, next_y, bricks):        
        row_idx = 0
        brick_idx = 0
        for row in bricks:
            brick_idx = 0
            for brick in row:
                if brick:
                    y = next_y + row_idx + 1
                    x = next_x + brick_idx
                    if (y >= BOARD_BLOCKS_H or
                        (x < 0 or x >= BOARD_BLOCKS_W)):
                        return self.ACTION_IMPACT
                    if self.board[y][x]:
                        return self.ACTION_IMPACT
                brick_idx+=1
            row_idx+=1        

        return self.NO_ACTION
    
    def burnin_current_block(self):
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

    def validate_rows(self):
        multiplayer = 0
        points = 0
        for row_idx in range(0,BOARD_BLOCKS_H):
            row = self.board[row_idx]
            print(row_idx,":",sum(row))
            if sum(row) == BOARD_BLOCKS_W:
                multiplayer+=1
                points+=POINTS_PER_ROW
                self.remove_row(row_idx)

        self.points += points * multiplayer

    def remove_row(self, row_idx):
        for i in reversed(range(1,row_idx+1)):
            self.board[i] = self.board[i-1]
    
    def left(self):
        if (self.simulate_action(
            self.current_block_x - 1, 
            self.current_block_y,
            self.current_block) == self.NO_ACTION):
            self.current_block_x-=1
    
    def right(self):
        if (self.simulate_action(
            self.current_block_x + 1, 
            self.current_block_y,
            self.current_block) == self.NO_ACTION):
            self.current_block_x+=1

    def rotate(self):
        self.current_block = rotate_matrix(self.current_block)
