import math


def solution(arr):
    answer = 1
    for a in arr:
        answer = int(answer * a / math.gcd(answer, a))
    return answer
