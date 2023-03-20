# 가운데를 말해요

# ---
# 시간 초과

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# N = int(input().strip())
# h = []
#
# for i in range(1, N + 1):
#     num = int(input().strip())
#     heapq.heappush(h, num)
#     temp = []
#     for idx in range(i):
#         cur = heapq.heappop(h)
#         if (i % 2 == 0 and idx == i // 2 - 1) or (i % 2 != 0 and idx == i // 2):
#             print(cur)
#         heapq.heappush(temp, cur)
#     h = temp

# ---
# Python 3 - 216 ms

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# N = int(input().strip())
# left_heap = []  # 최대 힙
# right_heap = []  # 최소 힙
#
# for i in range(1, N + 1):
#     num = int(input().strip())
#     if i == 1:
#         heapq.heappush(left_heap, -num)
#     else:
#         if len(left_heap) == len(right_heap):
#             if -left_heap[0] <= num <= right_heap[0]:
#                 heapq.heappush(left_heap, -num)
#             elif num <= -left_heap[0]:
#                 heapq.heappush(left_heap, -num)
#             elif num >= right_heap[0]:
#                 heapq.heappush(left_heap, -heapq.heappop(right_heap))
#                 heapq.heappush(right_heap, num)
#         elif len(left_heap) > len(right_heap):
#             if num <= -left_heap[0]:
#                 heapq.heappush(right_heap, -heapq.heappop(left_heap))
#                 heapq.heappush(left_heap, -num)
#             else:
#                 heapq.heappush(right_heap, num)
#     print(-left_heap[0])

# ---
# Python 3 - 236 ms

import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
left_heap = []  # 최대 힙
right_heap = []  # 최소 힙

for i in range(1, N + 1):
    num = int(input().strip())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and (-left_heap[0] > right_heap[0]):
        left_max = -heapq.heappop(left_heap)
        right_min = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -right_min)
        heapq.heappush(right_heap, left_max)

    print(-left_heap[0])
