from pathlib import Path
from level import Level, parse_level


class LevelLoader:
    def __init__(self, game, folder_path: str):
        self.game = game
        self.folder_path: str = folder_path
        self.levels: list[Level] = []
        self.curr_level = 0

    def load_levels(self):
        level_path = Path(self.folder_path)
        for item in level_path.iterdir():
            if item.is_file():
                level_text = item.read_text()
                self.levels.append(parse_level(self.game, level_text))
        self.levels.sort(key=lambda x: x.order)

    def get_next_level(self):
        if self.curr_level == 0:
            return self.levels[0]
        self.curr_level += 1
        return self.levels[self.curr_level]
