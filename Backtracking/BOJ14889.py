# 스타트와 링크

import sys

input = sys.stdin.readline

N = int(input().strip())
score = [list(map(int, input().split())) for _ in range(N)]

select = [False for _ in range(N)]
result = 9999


def func(cnt, idx):
    global result

    if cnt == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    start += score[i][j]
                elif not select[i] and not select[j]:
                    link += score[i][j]

        result = min(result, abs(start - link))
        return

    for i in range(idx, N):
        if not select[i]:
            select[i] = True
            func(cnt + 1, i + 1)
            select[i] = False


func(0, 0)
print(result)
