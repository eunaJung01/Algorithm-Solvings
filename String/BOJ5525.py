# IOIOI

import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
line = list(sys.stdin.readline().strip())

idx = 0
result = 0
pattern = 0

while idx < (M - 2):
    if line[idx] == 'I' and line[idx + 1] == 'O' and line[idx + 2] == 'I':
        pattern += 1
        if pattern == N:
            result += 1
            pattern -= 1
        idx += 2
    else:
        pattern = 0
        idx += 1

print(result)
