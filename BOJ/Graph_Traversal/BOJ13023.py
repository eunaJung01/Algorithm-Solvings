# ABCDE

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

friends = [[] for _ in range(N)]
for _ in range(M):
    f1, f2 = map(int, input().split())
    friends[f1].append(f2)
    friends[f2].append(f1)

visited = [False for _ in range(N)]
result = False


def DFS(friendNum, cnt):
    global visited, result
    if cnt == 5:
        result = True
        return

    friendList = friends[friendNum]
    for friend in friendList:
        if not visited[friend]:
            visited[friend] = True
            DFS(friend, cnt + 1)
            visited[friend] = False


for i in range(N):
    visited[i] = True
    DFS(i, 1)
    visited[i] = False
    if result:
        break

if result:
    print(1)
else:
    print(0)
