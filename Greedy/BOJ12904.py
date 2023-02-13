# A와 B

import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()

while len(T) > len(S):
    if T[-1] == "A":
        T = T[:-1]
    else:
        T = T[:-1][::-1]

if T == S:
    print(1)
else:
    print(0)
