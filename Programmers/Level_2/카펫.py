import math


def solution(brown, yellow):
    if yellow == 1:
        y = int(math.log2(brown + 1))
        return [y, y]

    for i in range(1, yellow // 2 + 1):
        if yellow % i > 0:
            continue

        y = i
        x = yellow // i

        if (y + 2) * 2 + x * 2 == brown:
            answer = [y + 2, x + 2]
            answer.sort(reverse=True)
            return answer

    assert False
