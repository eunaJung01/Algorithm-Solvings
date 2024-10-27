# 에너지 모으기

import sys

input = sys.stdin.readline

N = int(input().strip())
marble = list(map(int, input().split()))

result = 0
energy = 0


def func(marble):
    global result, energy

    if len(marble) == 2:
        result = max(result, energy)
        return

    for i in range(1, len(marble) - 1):  # 선택하는 구슬 번호
        mi = marble[i]
        m1 = marble[i - 1]
        m2 = marble[i + 1]

        energy += m1 * m2
        marble.pop(i)

        func(marble)

        marble.insert(i, mi)
        energy -= m1 * m2


func(marble)
print(result)
