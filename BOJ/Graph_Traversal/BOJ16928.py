# 뱀과 사다리 게임

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [0 for _ in range(101)]
visited = [False for _ in range(101)]

for _ in range(N + M):
    n1, n2 = map(int, input().split())
    board[n1] = n2


def BFS():
    q = deque()
    q.append((1, 0))  # 보드판 번호, 이동 횟수

    while q:
        b, n = q.popleft()
        visited[b] = True

        for i in range(1, 7):  # 주사위
            nb = b + i
            if 0 <= nb <= 100 and not visited[nb]:
                if nb == 100:
                    return n + 1
                if board[nb] != 0:
                    q.append((board[nb], n + 1))
                else:
                    q.append((nb, n + 1))


print(BFS())
