# 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

top = max(tree)
bottom = 0
mid = (top + bottom) // 2

while bottom <= top:
    mid = (top + bottom) // 2

    get = 0
    for t in tree:
        if t-mid > 0:
            get += t-mid

    if get >= M:
        bottom = mid + 1
    else:
        top = mid - 1

print(top)
