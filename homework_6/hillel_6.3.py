from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    sqrt_n = sqrt(n)
    i = 2
    while i <= sqrt_n:
        if n % i == 0:
            return False
        i += 1
    return True


print(is_prime(12))

# Good but no annotations in function and docstring.
# -1 point
