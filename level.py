import json
from entity import Entity, Objective, Wall, Blank, Box
from player import Player
from math import floor
class Level:
    def __init__(self, sk_game, name, order, map):
        self.sk_game = sk_game
        self.name: str = name
        self.order: int = order
        self.map: list[list[str]] = map
        self.entities: list[list[Entity]] = []
        self.objectives: list[Objective] = []
        self.offset_x = floor((16 - len(self.map[0]))/2)
        self.offset_y = floor((16 - len(self.map))/2)
        self.load_map()

    def load_map(self):
        for y in range(len(self.map)):
            row = []
            for x in range(len(self.map[y])):
                char = self.map[y][x]
                draw_x = self.offset_x
                draw_y = self.offset_y
                if char == "x":
                    row.append(Wall(self.sk_game, 'images/brick.png', x, y, draw_x, draw_y))
                elif char in ".":
                    row.append(Blank())
                elif char == "#":
                    row.append(Box(self.sk_game, 'images/box.png', x, y, draw_x, draw_y))
                elif char == "p":
                    self.player = Player(self.sk_game, 'images/gatito.png', x, y, draw_x, draw_y)
                    row.append(self.player)
                elif char == "o":
                    self.objectives.append(Objective(self.sk_game, 'images/objective.png', x, y, draw_x, draw_y))
                    row.append(Blank())
            self.entities.append(row)

    def blitme(self):
        for objective in self.objectives:
            objective.blitme()
        for row in self.entities:
            for entity in row:
                entity.blitme()

    def is_level_complete(self):
        for objective in self.objectives:
            if type(self.entities[objective.coord_y][objective.coord_x]) != Box:
                return False
        return True




def parse_level(game, text: str) -> Level:
    data: dict[str, str | list[str] | int] = json.loads(text)
    return Level(game, data["name"], data["order"], data["map"])
