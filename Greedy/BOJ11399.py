# ATM

import sys

N = int(sys.stdin.readline().strip())
time = list(map(int, sys.stdin.readline().split()))
time.sort(reverse=True)

result = 0
for i, t in enumerate(time):
    result += (i + 1) * t
print(result)
