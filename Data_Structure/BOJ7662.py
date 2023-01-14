# 이중 우선순위 큐

# 시간 초과
import sys
import heapq


def sync(heap):
    while heap and visited[heap[0][1]]:
        heapq.heappop(heap)


T = int(sys.stdin.readline().strip())
result = []

for _ in range(T):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙

    k = int(sys.stdin.readline().strip())
    visited = [False] * k
    for i in range(k):
        inst, num = map(str, sys.stdin.readline().strip().split())
        num = int(num)

        if inst == 'I':  # 정수 삽입
            heapq.heappush(min_heap, (num, i))  # 고유 번호 i
            heapq.heappush(max_heap, (-num, i))

        else:  # inst == 'D' : 정수 삭제
            if len(min_heap) != 0:
                if num == 1:  # 최댓값 삭제
                    sync(max_heap)
                    if max_heap:
                        max_value = heapq.heappop(max_heap)
                        visited[max_value[1]] = True
                    # min_heap.remove(heapq.heappop(max_heap)[1])

                elif num == -1:  # 최솟값 삭제
                    sync(min_heap)
                    if min_heap:
                        min_value = heapq.heappop(min_heap)
                        visited[min_value[1]] = True
                    # max_heap.remove((-min_value, min_value))

    sync(max_heap)
    sync(min_heap)

    if len(min_heap) == 0:
        result.append("EMPTY")
    else:
        result.append([-max_heap[0][0], min_heap[0][0]])

for r in result:
    if len(r) == 2:
        print(r[0], r[1])
    else:
        print(r)
