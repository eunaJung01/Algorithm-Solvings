# 용액

import sys

input = sys.stdin.readline

N = int(input().strip())
liquids = list(map(int, input().split()))
liquids.sort()

first, second = 0, N - 1
result = (liquids[first], liquids[second])

while first < second:
    pre_sum = result[0] + result[1]
    cur_sum = liquids[first] + liquids[second]

    if abs(pre_sum) >= abs(cur_sum):
        result = (liquids[first], liquids[second])

    if cur_sum < 0:
        first += 1
    else:
        second -= 1

print(str(result[0]) + " " + str(result[1]))
