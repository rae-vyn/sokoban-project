import sys

import pygame
from settings import Settings
from player import Player
# parts adapted from PCC chap. 14
class Game:
    def __init__(self):
        self.settings = Settings()
        dims = self.settings.tile_size_px * self.settings.grid_size

        pygame.init()
        self.screen = pygame.display.set_mode((dims, dims))
        self.clock = pygame.time.Clock()
        self.player = Player(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.player.blitme()
            pygame.display.flip()
            self.clock.tick(60) # run the game at 60fps
