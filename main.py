from typing import AnyStr

def module() -> int:
    print('Module')
    return 0

def echo(x: AnyStr) -> None:
    print(x)
    
def add(x: int, y: int = 0) -> int:
    return x + y

print("Hello world")