from pathlib import Path
from level import Level, parse_level


class LevelLoader:
    def __init__(self, folder_path: str):
        self.folder_path: str = folder_path
        self.levels: list[Level] = []

    def load_levels(self):
        level_path = Path(self.folder_path)
        for item in level_path.iterdir():
            if item.is_file():
                level_text = item.read_text()
                self.levels.append(parse_level(level_text))


loader = LevelLoader("./levels/")
loader.load_levels()
