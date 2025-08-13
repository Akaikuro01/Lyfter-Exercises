import json

class HandleJson():
    def __init__(self, path):
        self.path = path

    def write_json(self, elements):
        try:
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(elements, file, indent=4)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.path}")
        except PermissionError:
            raise PermissionError(f"Permission denied: {self.path}")
        except TypeError as ex:
            raise ValueError(f"Invalid data type for JSON: {ex}")
        except Exception as ex:
            raise Exception(f"Unexpected error writing JSON: {ex}")
        
        
        
    def read_json(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.path}")
        except PermissionError:
            raise PermissionError(f"Permission denied: {self.path}")
        except json.JSONDecodeError as ex:
            raise json.JSONDecodeError(
                f"Invalid JSON format in file {self.path}: {ex.msg}",
                ex.doc,
                ex.pos
            )
        except Exception as ex:
            raise Exception(f"Unexpected error reading JSON: {ex}")