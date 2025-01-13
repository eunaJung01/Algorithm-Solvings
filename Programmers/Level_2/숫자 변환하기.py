from collections import deque


def solution(x, y, n):
    if y == x:
        return 0

    q = deque()
    q.append((y, 0))
    visited = [False for _ in range(y)]

    while q:
        num, cnt = q.popleft()
        cnt += 1

        for next_num in (num / 2, num / 3, num - n):
            if not float(next_num).is_integer():
                continue

            next_num = int(next_num)
            if next_num == x:
                return cnt

            if next_num < x:
                continue
            if visited[next_num]:
                continue
            visited[next_num] = True
            q.append((next_num, cnt))

    return -1
