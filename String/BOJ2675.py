# 문자열 반복

import sys

T = int(sys.stdin.readline().strip())

result = []
for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    temp = []
    for s in S:
        for _ in range(int(R)):
            temp.append(s)
    result.append(''.join(temp))

for r in result:
    print(r)
