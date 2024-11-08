import pygame
import TetrisBoard
import Renderer
import GameController
from config import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H),pygame.RESIZABLE | pygame.SCALED)
game = GameController.GameControl(TetrisBoard.TetrisBoard(), Renderer.Renderer(screen))
game.run_loop()
pygame.quit()
