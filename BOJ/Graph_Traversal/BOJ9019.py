# DSLR

import sys
from collections import deque

input = sys.stdin.readline
T = int(input().strip())


def BFS(start, target):
    global visited
    q = deque()  # 현재 글자, 명령어
    q.append((start, ""))
    visited[start] = True

    while q:
        num, command = q.popleft()
        if num == target:
            return command

        for i in ["D", "S", "L", "R"]:
            new_num, new_command = 0, command + i

            if i == "D":
                new_num = (num * 2) % 10000
            elif i == "S":
                if num == 0:
                    new_num = 9999
                else:
                    new_num = num - 1
            elif i == "L":
                if num == 0:
                    continue
                new_num = (num % 1000) * 10 + num // 1000
            elif i == "R":
                if num == 0:
                    continue
                new_num = (num % 10) * 1000 + num // 10

            if not visited[new_num]:
                q.append((new_num, new_command))
                visited[new_num] = True


result = []
for _ in range(T):
    A, B = map(str, input().split())
    visited = [False for _ in range(10000)]
    result.append(BFS(int(A), int(B)))

for r in result:
    print(r)
