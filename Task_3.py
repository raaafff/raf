from math import floor


def zeros(n):
    z = 0
    while (n != 0):
        z += int(floor(n / 5))
        n /= 5
    return z


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
