import json
from typing import Tuple


class HandleJson():
    def __init__(self, path):
        self.path = path

    def write_json(self, elements):
        with open(self.path, "w") as file:
            json.dump(elements, file, indent=4)
        
    def read_json(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)