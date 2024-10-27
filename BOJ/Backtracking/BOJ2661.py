# 좋은수열

import sys


def isGoodArr(arr):
    for part_len in range(1, len(arr) // 2 + 1):
        for part_start in range(part_len, len(arr) - part_len + 1):
            if arr[part_start - part_len:part_start] == arr[part_start:part_start + part_len]:
                return False
    return True


def DFS(depth, arr):
    global status

    if status:
        return

    if depth == N:
        print("".join(list(map(str, arr))))
        status = True
        return

    arr.append(1)
    for i in range(1, 4):
        arr.pop()
        arr.append(i)
        if isGoodArr(arr):
            if not DFS(depth + 1, arr):
                continue
    else:
        arr.pop()
        return False


N = int(sys.stdin.readline().strip())
status = False
result = DFS(0, [])
