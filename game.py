import sys

import pygame
from settings import Settings
from player import Player
from entity import Entity
from text import Text
from level import Level, parse_level
from levelloader import LevelLoader


# parts adapted from PCC chap. 14
class Game:
    def __init__(self):
        self.settings = Settings()
        dims = self.settings.tile_size_px * self.settings.grid_size
        pygame.init()
        # dims is x and y because the game's in a square window.
        self.screen = pygame.display.set_mode((dims, dims))
        self.clock = pygame.time.Clock()
        self.level_loader = LevelLoader(self, "./levels/")
        self.curr_level = self.level_loader.load_levels()
        self.thanks_text = Text(self, "Thanks for playing! You win!")
        if self.curr_level.player:
            self.player: Player = self.curr_level.player
        else:  # This is mainly to make sure that the map was made correctly.
            raise Exception("No player in the map!")

    # draw the tiling background. I'm not super sure if this is that efficient, honestly.
    def draw_background(self):
        for x in range(0, 16):
            for y in range(0, 16):
                tile_image = pygame.image.load("images/bg.png")
                tile_rect = tile_image.get_rect()
                tile_rect.x = x * self.settings.tile_size_px
                tile_rect.y = y * self.settings.tile_size_px
                self.screen.blit(tile_image, tile_rect)

    def run_game(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:  # exit the game
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.curr_level:  # reset the level
                        self.curr_level.load_map()
                        self.player = self.curr_level.player

            if not self.curr_level:  # passed the last level
                self.thanks_text.draw_text()
                pygame.display.flip()
                self.clock.tick(60)
                continue  # just keep the game window open

            # Check for input from the player
            self.player.check_events(events)

            # Drawing step
            self.screen.fill(self.settings.bg_color)
            self.draw_background()
            self.player.blitme()
            self.curr_level.blitme()

            # Progress levels
            if self.curr_level.is_level_complete():
                self.curr_level = self.level_loader.get_next_level()
                if self.curr_level:
                    self.player = self.curr_level.player

            # Refresh the screen at 60 fps
            pygame.display.flip()
            self.clock.tick(60)
