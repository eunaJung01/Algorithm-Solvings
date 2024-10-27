# 링크와 스타트

import sys


def calculate_abilities():
    global result
    start, link = 0, 0

    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:  # start team
                start += abilities[i][j]
            elif not visited[i] and not visited[j]:  # link team
                link += abilities[i][j]

    result = min(result, abs(start - link))


def build_team(count):
    if count == N:
        calculate_abilities()
        return

    visited[count] = 1  # start team
    build_team(count + 1)

    visited[count] = 0  # link team
    build_team(count + 1)


N = int(sys.stdin.readline().strip())
visited = [0] * N  # start : 1 / link : 0

abilities = []
for _ in range(N):
    abilities.append(list(map(int, sys.stdin.readline().split())))

result = 99999999
build_team(0)
print(result)
