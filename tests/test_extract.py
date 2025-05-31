from pathlib import Path

from klaradvn.extract import extract_function_code, extract_class

PATH_PACKAGE = Path(__file__).parent / 'test-package'

def test_extract_function_code():
    f, path = extract_function_code(str(PATH_PACKAGE), 'lorem_ipsum')
    val = """def lorem_ipsum():
    a = 2
    if a > 3:
        print('a is more than 3')
    lorem_ipsum_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\\n" 
    lorem_ipsum_text += "Duis ac dui tortor. Nullam dapibus metus ut nibh egestas, a ultricies tellus placerat.\\n"
    lorem_ipsum_text += "Fusce vestibulum libero nec justo condimentum dignissim. Vivamus euismod turpis quis leo efficitur blandit.\\n"
    lorem_ipsum_text += "Aliquam erat volutpat. Sed id nisl eu nisi lobortis elementum in vel mi. Maecenas eu felis non velit dictum pretium.\\n"
    lorem_ipsum_text += "Integer vestibulum, justo sit amet fringilla pharetra, orci nulla malesuada lectus, vitae finibus metus odio ac libero.\\n"
    lorem_ipsum_text += "Sed ac turpis ut ante bibendum imperdiet. In hac habitasse platea dictumst. Sed at dolor id sapien gravida condimentum non vel eros.\\n"
    lorem_ipsum_text += "Nulla facilisi. Vivamus posuere lacinia ipsum in rutrum. Maecenas auctor, nunc et vestibulum pulvinar, purus turpis varius nulla, eu tincidunt libero leo nec justo."
    
    # Split the text into lines and return the first 10
    return lorem_ipsum_text.split('\\n')"""
    assert f == val
    assert Path(path) == Path(__file__).parent / 'test-package' / 'package_one' / 'lorem_ipsum.py'

def test_extract_another_function():
    f, _ = extract_function_code(str(PATH_PACKAGE), 'another_function')
    val = """def another_function(
    n1: int,
    n2: int
):
    return n2 > n1"""
    assert f == val

def test_extract_class_dataclass():
    result = extract_class(PATH_PACKAGE, 'CoolNewList')
    assert result['source_code'] == """@dataclass
class CoolNewList:
    elements: list[int]

    def add_element(self, n: int):
        self.elements.append(n)
    
    def remove_element(self, idx: int):
        if idx > len(self.elements) - 1:
            raise IndexError(f"List is only {len(self.elements)} long, the index you provided: {idx} does not exist")
        self.elements.pop(idx)
    
    def reverse(self):
        self.elements.reverse()"""

def test_extract_class_custom():
    result = extract_class(PATH_PACKAGE, 'MyCustomObject')
    assert result['source_code'] == """class MyCustomObject:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def shift_x(self, shift: int):
        self.x += shift
    
    def get_coords(self) -> tuple[int, int]:
        return self.x, self.y"""