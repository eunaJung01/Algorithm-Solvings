# 새

import sys

N = int(sys.stdin.readline().strip())

result = 0

sing = 1
while True:
    if N <= 0:
        break
    if N < sing:
        sing = 1
        continue
    N -= sing
    sing += 1
    result += 1

print(result)
