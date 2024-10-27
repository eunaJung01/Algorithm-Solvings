# 주사위

import sys

input = sys.stdin.readline

N = int(input().strip())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
else:
    A, B, C, D, E, F = map(int, dice)
    min_one = min(dice)
    min_two = min(A + B, A + C, A + D, A + E, B + C, C + E, E + D, D + B, B + F, C + F, D + F, E + F)
    min_three = min(A + B + C, A + C + E, A + E + D, A + D + B, F + B + C, F + C + E, F + E + D, F + D + B)

    ans = 0
    # N-1층 (맨 위)
    ans += min_one * (N - 2) * (N - 2) + (min_two * (N - 2) + min_three) * 4
    # 0 ~ N-2층
    ans += (min_one * (N - 2) + min_two) * 4 * (N - 1)
    print(ans)
