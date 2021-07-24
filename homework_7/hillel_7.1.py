# map function replacement
def custom_map(func, args: list) -> list:
    result = []
    for i in args:
        result.append(func(i))
    return result



