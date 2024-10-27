# A+B - 8

import sys

input = sys.stdin.readline

T = int(input().strip())
cases = [list(map(int, input().split())) for _ in range(T)]

for i, case in enumerate(cases):
    a, b = map(int, case)
    print("Case #" + str(i + 1) + ": " + str(a) + " + " + str(b) + " = " + str(a + b))
