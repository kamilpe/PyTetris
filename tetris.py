import pygame

BRICK_SIZE = 29
PLAYFIELD_W = 10
PLAYFIELD_H = 12

tetronimos = [
    [[8,9,10,11], [2,6,10,14]], # Long
    [[0,1,4,5]], # Box
    [[4,5,6,10], [1,5,8,9], [0,4,5,6], [1,2,5,9]], # L1
    [[4,5,6,8], [0,1,5,9], [2,4,5,6], [1,5,9,10]], # L2
    [[5,6,8,9], [0,4,5,9]], # S
    [[8,9,13,14], [1,4,5,8]], # Z
    [[4,5,6,9],[4,1,5,9],[1,4,5,6],[1,5,6,9]] # T
]

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(
    (PLAYFIELD_W*(BRICK_SIZE+2), 
     PLAYFIELD_H*(BRICK_SIZE*2)))

