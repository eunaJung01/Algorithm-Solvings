from collections import deque


def BFS(start, n, computers, visited):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()

        for next in range(n):
            if computers[cur][next] == 1 and not visited[next]:
                visited[next] = True
                q.append(next)


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            answer += 1
            BFS(i, n, computers, visited)

    return answer
