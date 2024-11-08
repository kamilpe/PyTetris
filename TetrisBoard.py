import random
import pygame
import patterns
from config import *


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
        self.points = 0
        random.seed(pygame.time.get_ticks())
        self.inject(self.get_random_pattern())
        self.set_next_pattern(self.get_random_pattern())
    
    def inject(self, pattern):
        random.seed(pygame.time.get_ticks())
        self.set_cur_pattern(pattern)
        
        block_width = len(self.cur_block)
        self.current_block_x = int(BOARD_BLOCKS_W / 2 - block_width / 2)
        self.current_block_y = 0

    def set_cur_pattern(self, pattern):
        self.cur_pattern_idx = pattern[0]
        self.cur_pattern_orientation = pattern[1]
        self.cur_block = patterns.get_block(self.cur_pattern_idx, self.cur_pattern_orientation)

    def set_next_pattern(self, pattern):
        self.next_pattern_idx = pattern[0]
        self.next_pattern_orientation = pattern[1]
        self.next_block = patterns.get_block(self.next_pattern_idx, self.next_pattern_orientation)

    def get_random_pattern(self):
        patternId = random.randint(0, patterns.PATTERNS_COINT-1)
        orientation = random.randint(0, patterns.ORIENTATION_COUNT-1)
        return (patternId, orientation)

    def advance(self):
        if (self.simulate_action(
            self.current_block_x, 
            self.current_block_y, 
            self.cur_block) == self.ACTION_IMPACT):

            self.burnin_current_block()
            self.inject((self.next_pattern_idx, self.next_pattern_orientation))
            self.set_next_pattern(self.get_random_pattern())
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
        for row in self.cur_block:
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
            self.cur_block) == self.NO_ACTION):
            self.current_block_x-=1
    
    def right(self):
        if (self.simulate_action(
            self.current_block_x + 1, 
            self.current_block_y,
            self.cur_block) == self.NO_ACTION):
            self.current_block_x+=1

    def rotate(self):
        if self.cur_pattern_orientation < patterns.ORIENTATION_COUNT-1:
            self.set_cur_pattern((self.cur_pattern_idx, self.cur_pattern_orientation+1))
        else:
            self.set_cur_pattern((self.cur_pattern_idx, 0))
