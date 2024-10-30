import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = []
    for work in works:
        heapq.heappush(heap, -work)

    for _ in range(n):
        heapq.heappush(heap,
                       heapq.heappop(heap) + 1)

    return sum([i ** 2 for i in heap])
