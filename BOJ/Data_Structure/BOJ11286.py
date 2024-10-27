# 절댓값 힙

import sys
import heapq

N = int(sys.stdin.readline().strip())
numList = []
heap = []  # 최소 힙
result = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())

    # 절댓값이 가장 작은 값 pop
    # 절댓값이 가장 작은 값이 여러 개일 때는, 가장 작은 수를 출력
    if num == 0:
        if len(heap) == 0:
            result.append(0)
        else:
            temp = heapq.heappop(heap)
            if temp > 0:
                if -temp in numList:
                    result.append(-temp)
                    numList.pop(numList.index(-temp))
                    continue
            result.append(temp)
            numList.pop(numList.index(temp))

    # 삽입
    else:
        numList.append(num)
        heapq.heappush(heap, abs(num))  # 절댓값 push

for r in result:
    print(r)
