# filter function replacement
def custom_filter(func, args: list) -> list:
    result = []
    for i in args:
        if func(i):
            result.append(i)
        else:
            continue
    return result







