from dataclasses import dataclass

@dataclass
class CoolNewList:
    elements: list[int]

    def add_element(self, n: int):
        self.elements.append(n)
    
    def remove_element(self, idx: int):
        if idx > len(self.elements) - 1:
            raise IndexError(f"List is only {len(self.elements)} long, the index you provided: {idx} does not exist")
        self.elements.pop(idx)
    
    def reverse(self):
        self.elements.reverse()

class MyCustomObject:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def shift_x(self, shift: int):
        self.x += shift
    
    def get_coords(self) -> tuple[int, int]:
        return self.x, self.y