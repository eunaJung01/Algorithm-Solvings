# 서로 다른 부분 문자열의 개수

import sys

S = sys.stdin.readline().strip()

strings = set()
for start in range(len(S)):
    for end in range(start + 1, len(S) + 1):
        strings.add(S[start:end])
print(len(strings))
