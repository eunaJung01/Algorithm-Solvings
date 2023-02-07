# 숨바꼭질 5

import sys

input = sys.stdin.readline

max_pos = 500000
visited = [[False] * (max_pos + 1) for _ in range(2)]
N, K = map(int, input().split())  # 수빈, 동생


def BFS():
    global N, K
    q = [N]
    visited[0][N] = True
    flag = 0
    time = 0

    while q:
        if K > max_pos:
            break
        if visited[flag][K]:
            return time

        new_q = []
        flag = 1 - flag
        for pos in q:
            for nextPos in (pos - 1, pos + 1, pos * 2):
                if 0 <= nextPos <= max_pos and not visited[flag][nextPos]:
                    visited[flag][nextPos] = True
                    new_q.append(nextPos)
        time += 1
        K += time
        q = new_q

    return -1


print(BFS())
