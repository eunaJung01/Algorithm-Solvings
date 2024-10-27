# 히스토그램

import sys

input = sys.stdin.readline

N = int(input().strip())
heights = [int(input().strip()) for _ in range(N)]


def solve(left, right):
    global heights
    if left == right:
        return heights[left]

    mid = (left + right) // 2
    result = max(solve(left, mid), solve(mid + 1, right))

    p1, p2 = mid, mid + 1
    height = min(heights[p1], heights[p2])
    result = max(result, height * 2)

    while left < p1 or p2 < right:
        if p2 < right and (p1 == left or heights[p1 - 1] < heights[p2 + 1]):
            p2 += 1
            height = min(height, heights[p2])
        else:
            p1 -= 1
            height = min(height, heights[p1])
        result = max(result, height * (p2 - p1 + 1))

    return result


print(solve(0, N - 1))
