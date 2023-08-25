"""
練習問題を解いたときのコード
"""

# (1)
def print_hello(count: int):
    print(count * "Hello")


# (2)
def get_rectangle_area(width: float, height: float) -> float:
    return width * height


# (3)
def get_message(name: str):
    print(f"こんにちは{name}さん")


# (4)
def get_absolute_value(value: float) -> float:
    return abs(value)


# (5)
def get_tail(*args):
    return args[-1]


print_hello(3)
print(get_rectangle_area(3, 5))
get_message("John")
print(get_absolute_value(5.2))
print(get_absolute_value(-3.3))
print(get_tail(3, 5, 9, 2))
