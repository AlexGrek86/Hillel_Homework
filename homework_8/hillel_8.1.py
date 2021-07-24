def decorator_func(func):
    def wrapper():
        print(func.__name__)
        func(a, b)

    return wrapper()


a = 2
b = 2


@decorator_func
def sum_1(a: int, b: int) -> int:
    return print(a + b)


@decorator_func
def multiplication(a: int, b: int) -> int:
    return print(a * b)
