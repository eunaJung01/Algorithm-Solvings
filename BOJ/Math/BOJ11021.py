# A+B - 7

import sys

input = sys.stdin.readline

T = int(input().strip())

result = []
for _ in range(T):
    A, B = map(int, input().split())
    result.append(A + B)

for i, r in enumerate(result):
    print("Case #" + str(i + 1) + ": " + str(r))
