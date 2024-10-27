# 스택 수열

import sys

n = int(sys.stdin.readline())

count = 1
stack = []
result_string = []
result = True

for _ in range(1, n + 1):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        result_string.append("+")
        count += 1

    if stack[-1] == num:
        stack.pop(-1)
        result_string.append("-")
    else:
        result = False

if not result:
    print("NO")
else:
    for r in result_string:
        print(r)
