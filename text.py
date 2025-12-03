# Based off of PCC: Chapter 14
from typing import TYPE_CHECKING
import pygame.font

if TYPE_CHECKING:
    from game import Game

class Text:
    def __init__(self, sk_game: 'Game', text):
        self.screen = sk_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sk_game.settings
        self.text_color = (0, 0, 0) # Black
        self.font = pygame.font.SysFont(None, 48)
        self.prep_text(text)

    def prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color, self.settings.bg_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.midbottom = self.screen_rect.midbottom
        self.text_image_rect.y -= 3 * self.settings.tile_size_px

    def draw_text(self):
        self.screen.blit(self.text_image, self.text_image_rect)
