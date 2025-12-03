import pygame

from settings import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class Entity:
    def __init__(self, sk_game: "Game", image_path, coord_x=0, coord_y=0, draw_x=0, draw_y=0):
        self.sk_game = sk_game
        self.screen = self.sk_game.screen
        self.screen_rect = self.sk_game.screen.get_rect()
        self.image = pygame.image.load(image_path)
        self.settings = Settings()
        self.image = pygame.transform.scale(
            self.image, (self.settings.tile_size_px, self.settings.tile_size_px)
        )
        self.rect = self.image.get_rect()
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.draw_x = draw_x
        self.draw_y = draw_y
        self.rect.y = (self.coord_y + draw_y) * self.settings.tile_size_px
        self.rect.x = (self.coord_x + draw_x) * self.settings.tile_size_px

    def move(self, move_x, move_y):
        move_attempt = self.sk_game.curr_level.entities[self.coord_y + move_y][self.coord_x + move_x]
        # Swap the two tiles in the grid so we can keep the record updated
        self.sk_game.curr_level.entities[self.coord_y + move_y][self.coord_x + move_x] = self
        self.sk_game.curr_level.entities[self.coord_y][self.coord_x] = move_attempt

        self.coord_x += move_x
        self.coord_y += move_y
        self.rect.x = (self.coord_x + self.draw_x) * self.settings.tile_size_px
        self.rect.y = (self.coord_y + self.draw_y) * self.settings.tile_size_px

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Wall(Entity):
    def __init__(self, sk_game: "Game", image_path, coord_x=0, coord_y=0, draw_x=0, draw_y=0):
        super().__init__(sk_game, image_path, coord_x, coord_y, draw_x, draw_y)


class Box(Entity):
    def __init__(self, sk_game: "Game", image_path, coord_x=0, coord_y=0, draw_x=0, draw_y=0):
        super().__init__(sk_game, image_path, coord_x, coord_y, draw_x, draw_y)

    def can_move(self, move_x, move_y) -> bool:
        move_attempt = self.sk_game.curr_level.entities[self.coord_y + move_y][self.coord_x + move_x]
        print(type(move_attempt))
        if type(move_attempt) in (Blank, Objective):
            return True
        return False


class Objective(Entity):
    def __init__(self, sk_game: "Game", image_path, coord_x=0, coord_y=0, draw_x=0, draw_y=0):
        super().__init__(sk_game, image_path, coord_x, coord_y, draw_x, draw_y)
        self.completed = False  # is a box on the coordinate


class Blank(Entity):  # Blank Placeholder
    def __init__(self):
        return

    def blitme(self):
        return
