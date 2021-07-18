from math import sqrt


def square(sd):
    perimetr = 4 * sd
    area = pow(sd, 2)
    diagonal = round((sd * sqrt(2)), 2)
    result = (perimetr, area, diagonal)

    return result


print(square(5))

# Good but sd not clear argument. No docstrings which can described what is it
# and not annotations.
# - 1 points
