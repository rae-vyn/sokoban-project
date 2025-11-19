import json


class Level:
    def __init__(self, name, order, map):
        self.name = name
        self.order = order
        self.map = map


def parse_level(text: str) -> Level:
    data: dict[str, str | list[str]] = json.loads(text)
    print(data)
    return Level(data["name"], data["order"], data["map"])
