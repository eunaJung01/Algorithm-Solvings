from math import sqrt


def solution(n):
    x = int(sqrt(n))
    if x ** 2 != n:
        return -1
    return (x + 1) ** 2
