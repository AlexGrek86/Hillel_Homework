numbers = 1000


# TODO: incoarrect generator was provided. Generator should return ** 2 for each element
def generator_function(number: int):
    for i in range(number):
        if i % 2 == 0:
            yield i


# TODO: incorrect annotation for return type was addeed
def result_arithmetic() -> print():
    for item in generator_function(numbers):
        print(pow(item, 2))


print(result_arithmetic())

# -10 points
