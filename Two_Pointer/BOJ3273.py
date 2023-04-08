# 두 수의 합

import sys

input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split()))
numbers.sort()
x = int(input().strip())

first, second = 0, n - 1
cnt = 0

while first < second:
    s = numbers[first] + numbers[second]
    if s == x:
        cnt += 1
        first += 1
        continue
    if s < x:
        first += 1
    else:
        second -= 1

print(cnt)
