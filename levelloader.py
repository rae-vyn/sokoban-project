from pathlib import Path
from typing import TYPE_CHECKING
from level import Level, parse_level

if TYPE_CHECKING:
    from game import Game


class LevelLoader:
    def __init__(self, game: "Game", folder_path: str):
        self.game = game
        self.folder_path: str = folder_path
        self.levels: list[Level] = []
        self.curr_level = 0

    def load_levels(self):
        level_path = Path(self.folder_path)
        for item in level_path.iterdir():
            if item.is_file() and item.name.endswith(".json"):
                level_text = item.read_text().strip()
                self.levels.append(parse_level(self.game, level_text))
        self.levels.sort(key=lambda x: x.order)
        return self.levels[0]

    def get_next_level(self):
        self.curr_level += 1
        try:
            return self.levels[self.curr_level]
        except IndexError:
            return None
