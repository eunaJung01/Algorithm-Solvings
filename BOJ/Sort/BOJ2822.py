# 점수 계산

import sys

input = sys.stdin.readline
score = []
for i in range(8):
    score.append((int(input().strip()), i))
score.sort()
score = score[-5:]

sum = 0
num = []
for s in score:
    sum += s[0]
    num.append(s[1] + 1)
num.sort()

print(sum)
for n in num:
    print(n, end=' ')
