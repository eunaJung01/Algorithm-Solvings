# 케빈 베이컨의 6단계 법칙

import sys

N, M = map(int, sys.stdin.readline().split())  # N : 유저의 수 / M : 친구 관계의 수

INF = int(1e9)  # infinite
friend = [[INF for _ in range(N)] for _ in range(N)]  # 친구 리스트 (0 ~ N-1)

for _ in range(M):
    f1, f2 = map(int, sys.stdin.readline().split())
    f1 -= 1
    f2 -= 1
    friend[f1][f2] = 1
    friend[f2][f1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if friend[i][j] > friend[i][k] + friend[k][j]:
                friend[i][j] = friend[i][k] + friend[k][j]

for i in range(N):
    result = 0
    for j in range(N):
        if friend[i][j] != 999:
            result += friend[i][j]
    friend[i] = (result, i + 1)

friend.sort()
print(friend[0][1])
