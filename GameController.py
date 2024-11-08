import pygame

class GameControl:
    def __init__(self, board, renderer):
        self.board = board
        self.renderer = renderer
        self.clock = pygame.time.Clock()
        self.last_tick = pygame.time.get_ticks()        
        self.current_delay = 750
        self.target_delay = 750
        self.running = True

    def run_loop(self):
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
