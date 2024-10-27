# AC

import sys
from collections import deque


def get_result(func, arr):
    global result
    reverse = False

    for f in func:
        if f == "R":  # 뒤집기
            reverse = True if not reverse else False

        elif f == "D":  # 첫번째 수 버리기
            if len(arr) == 0:
                result.append("error")
                return
            if not reverse:
                arr.popleft()
            else:
                arr.pop()

    r = ""
    if not reverse:
        for i in range(len(arr)):
            r += str(arr[i]) + ','
    else:
        for i in range(len(arr) - 1, -1, -1):
            r += str(arr[i]) + ','
    r = "[" + r[:-1] + "]"

    result.append(r)


T = int(sys.stdin.readline().strip())

result = []
for _ in range(T):
    func = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()

    arr = []
    if line == "[]":
        arr = deque()
    else:
        arr = deque(map(int, line[1:-1].split(',')))

    get_result(func, arr)

for r in result:
    print(r)
