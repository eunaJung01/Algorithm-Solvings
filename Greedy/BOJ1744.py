# 수 묶기

import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
result = 0

if N == 1:
    result = int(input().strip())
else:
    pos, neg, hasZero = [], [], False
    for _ in range(N):
        num = int(input().strip())
        if num > 0:
            heapq.heappush(pos, -num)
        elif num <= 0:
            heapq.heappush(neg, num)
        else:
            hasZero = True

    while len(pos) >= 2:
        first, second = -heapq.heappop(pos), -heapq.heappop(pos)
        if first == 1 or second == 1:
            result += first + second
            continue
        result += first * second
    if pos:
        result += -heapq.heappop(pos)

    if len(neg) % 2 == 0:  # 음수 짝수개
        while len(neg) >= 2:
            result += heapq.heappop(neg) * heapq.heappop(neg)
    else:
        if hasZero:
            neg.pop(neg.index(max(neg)))
        while len(neg) >= 2:
            result += heapq.heappop(neg) * heapq.heappop(neg)
        if neg:
            result += heapq.heappop(neg)

print(result)
