# 요세푸스 문제 0

import sys

N, K = map(int, sys.stdin.readline().split())
people = [i for i in range(1, N + 1)]

idx = K - 1
result = []
while True:
    result.append(people[idx])
    people.pop(idx)
    if people:
        idx = (idx + K - 1) % len(people)
    else:
        break

print("<", end='')
for i, r in enumerate(result):
    if i != N - 1:
        print(str(r) + ", ", end='')
    else:
        print(r, end='')
print(">")
