# 계란으로 계란치기

import sys

input = sys.stdin.readline

N = int(input().strip())

S = []  # 내구도
W = []  # 무게
for _ in range(N):
    s, w = map(int, input().split())
    S.append(s)
    W.append(w)

result = 0


def func(cnt):
    global result

    if cnt == N:
        temp = 0
        for i in range(N):
            if S[i] <= 0:
                temp += 1
        result = max(result, temp)
        return

    if S[cnt] <= 0:
        func(cnt + 1)
        return

    status = False
    for j in range(N):  # 칠 계란
        if S[j] > 0 and cnt != j:
            status = True

            S[cnt] -= W[j]
            S[j] -= W[cnt]

            func(cnt + 1)

            S[cnt] += W[j]
            S[j] += W[cnt]

    if not status:
        func(cnt + 1)


func(0)
print(result)
