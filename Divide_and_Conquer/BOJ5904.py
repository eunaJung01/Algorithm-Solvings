# Moo 게임

import sys


def moo(total_moo, mid_moo, N):
    prev_moo = (total_moo - mid_moo) // 2
    if N <= prev_moo:
        return moo(prev_moo, mid_moo - 1, N)
    if N > prev_moo + mid_moo:
        return moo(prev_moo, mid_moo - 1, N - prev_moo - mid_moo)
    return "o" if N - prev_moo - 1 else "m"


N = int(sys.stdin.readline().strip())

total_moo, mid_moo = 3, 0
while N > total_moo:
    mid_moo += 1
    total_moo = total_moo * 2 + mid_moo + 3

print(moo(total_moo, mid_moo + 3, N))
