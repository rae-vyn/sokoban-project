import sys

import pygame
from settings import Settings
from player import Player
from entity import Entity
from level import Level, parse_level
from levelloader import LevelLoader
# parts adapted from PCC chap. 14
class Game:
    def __init__(self):
        self.settings = Settings()
        dims = self.settings.tile_size_px * self.settings.grid_size

        pygame.init()
        self.screen = pygame.display.set_mode((dims, dims))
        self.clock = pygame.time.Clock()
        self.level_loader = LevelLoader(self, './levels/')
        self.level_loader.load_levels()
        self.curr_level = self.level_loader.get_next_level()
        if self.curr_level.player:
            self.player: Player = self.curr_level.player
        else:
            raise Exception("No player in the map!")


    def run_game(self):
        while True:
            events = pygame.event.get()
            self.player.check_events(events)
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.player.blitme()
            self.curr_level.blitme()
            if self.curr_level.is_level_complete():
                self.curr_level = self.level_loader.levels[self.curr_level.order]
                self.player = self.curr_level.player
            pygame.display.flip()
            self.clock.tick(60) # run the game at 60fps
