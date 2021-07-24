numbers = 1000


def generator_function(number: int):
    for i in range(number):
        if i % 2 == 0:
            yield i


def result_arithmetic() -> print():
    for item in generator_function(numbers):
        print(pow(item, 2))


print(result_arithmetic())
