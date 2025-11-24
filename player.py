import pygame

from settings import Settings

# adapted from PCC chap. 14
class Player:
    def __init__(self, sk_game):
        self.screen = sk_game.screen
        self.screen_rect = sk_game.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load('images/gatito.png')
        self.image = pygame.transform.scale(self.image, (self.settings.tile_size_px, self.settings.tile_size_px))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def check_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rect.x += self.settings.tile_size_px
                if event.key == pygame.K_LEFT:
                    self.rect.x -= self.settings.tile_size_px
                if event.key == pygame.K_DOWN:
                    self.rect.y += self.settings.tile_size_px
                if event.key == pygame.K_UP:
                    self.rect.y -= self.settings.tile_size_px

    def blitme(self):
        self.screen.blit(self.image, self.rect)
