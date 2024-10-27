# 프린터 큐

from collections import deque

import sys

num = int(sys.stdin.readline())

for _ in range(num):
    N, M = map(int, sys.stdin.readline().split())  # N : 문서의 개수 / M : 몇번째로 인쇄 되었는지 확인해야 하는 문서의 위치
    queue = deque([i for i in map(int, sys.stdin.readline().split())])

    count = 0
    while len(queue) != 0:
        if len(queue) == 1:
            count += 1
            queue.popleft()

        elif queue[0] < max(queue):  # 뒤로 재배치
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1
            queue.append(queue.popleft())
        else:  # 인쇄
            if M == 0:
                count += 1
                break
            else:
                M -= 1
                queue.popleft()
                count += 1

    print(count)
