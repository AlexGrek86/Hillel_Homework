# map function replacement
def custom_map(func, args: list) -> list:
    result = []
    for i in args:
        result.append(func(i))
    return result


if __name__ == '__main__':
    print(custom_map(lambda item: item * 2, [1, 2, 3, 4, 5]))

# too much empty lines in the end of module
# -1 point
