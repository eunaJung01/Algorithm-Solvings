# 종이의 개수

import sys

input = sys.stdin.readline

N = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(N)]

result = [0] * 3  # -1, 0, 1


def count(n, y, x):
    s = paper[y][x]
    if n > 1:
        for i in range(y, y + n):
            for j in range(x, x + n):

                if s != paper[i][j]:
                    for ny in range(3):
                        for nx in range(3):
                            count(n // 3, y + ny * n // 3, x + nx * n // 3)
                    return

        result[s + 1] += 1

    else:
        result[s + 1] += 1


count(N, 0, 0)
for r in result:
    print(r)
