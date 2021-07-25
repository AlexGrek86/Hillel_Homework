# filter function replacement
def custom_filter(func, args: list) -> list:
    result = []
    for i in args:
        if func(i):
            result.append(i)
        else:
            continue
    return result





if __name__ == '__main__':
    print(custom_filter(lambda item: item > 5, [3, 4, 5, 6]))

# too much empty lines in the end of module
# -1 point
