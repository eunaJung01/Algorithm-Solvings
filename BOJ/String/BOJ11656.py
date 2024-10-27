# 접미사 배열

import sys

input = sys.stdin.readline
S = input().strip()

result = []
for i in range(len(S)):
    result.append(S[i:])
result.sort()

for r in result:
    print(r)
