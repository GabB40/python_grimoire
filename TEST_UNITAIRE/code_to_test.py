def add(a: int|str, b: int|str):
    if not (type(a) in [str, int] or type(b) in [str, int]):
        print("Wrong types")
        return False
    return int(a) + int(b)