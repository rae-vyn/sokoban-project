import pygame
from pprint import pprint
from entity import Entity, Wall, Blank, Box
from settings import Settings

# adapted from PCC chap. 14
class Player(Entity):
    def __init__(self, sk_game, image_path, coord_x=0, coord_y=0, draw_x=0, draw_y = 0):
        super().__init__(sk_game, image_path, coord_x, coord_y, draw_x, draw_y)

    def check_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                move_x = 0
                move_y = 0
                if event.key == pygame.K_RIGHT:
                    move_x = 1
                elif event.key == pygame.K_LEFT:
                    move_x = -1
                if event.key == pygame.K_DOWN:
                    move_y = 1
                elif event.key == pygame.K_UP:
                    move_y = -1
                self.handle_collision(move_x, move_y)

    def handle_collision(self, move_x, move_y):
        if not self.sk_game.curr_level: # so type checking leaves me alone
            return
        # Check the grid to move the player
        move_attempt = self.sk_game.curr_level.entities[self.coord_y + move_y][self.coord_x + move_x]
        if type(move_attempt) == Blank:
            self.move(move_x, move_y)
        if type(move_attempt) == Box:
            # move the box in the same direction we move the character.
            if move_attempt.can_move(move_x, move_y):
                move_attempt.move(move_x, move_y)
                self.move(move_x, move_y)
