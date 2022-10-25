# 기상캐스터

import sys

input = sys.stdin.readline

H, W = map(int, input().split())
cloud = []
for _ in range(H):
    temp = []
    line = input().strip()
    for l in line:
        if l == 'c':
            temp.append(1)
        else:
            temp.append(0)
    cloud.append(temp)

result = [[-1 for _ in range(W)] for _ in range(H)]

for i in range(H):
    no_cloud = []
    for j in range(W - 1, -1, -1):
        if cloud[i][j] == 1:
            result[i][j] = 0
            for n in no_cloud:
                result[i][n] = n - j
            no_cloud = []
        else:
            no_cloud.append(j)

for row in result:
    for r in row:
        print(r, end=' ')
    print()
