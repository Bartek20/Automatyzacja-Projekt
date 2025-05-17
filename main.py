from typing import AnyStr

def module() -> int:
    print('Module')
    return 0

def echo(x: AnyStr) -> None:
    print(x)

print("Hello world")