# 수 찾기

# import sys
#
# input = sys.stdin.readline
#
# N = int(input().strip())
# A = list(map(int, input().split()))
# A.sort()
#
# M = int(input().strip())
# B = list(map(int, input().split()))
# for b in B:
#     if b in A:
#         print(1)
#     else:
#         print(0)

# 이분 탐색

import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

M = int(input().strip())
B = list(map(int, input().split()))


def binarySearch(num, lst):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if num == lst[mid]:
            return 1
        elif num < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for b in B:
    print(binarySearch(b, A))
