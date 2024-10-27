# 생일

import sys

input = sys.stdin.readline
n = int(input().strip())

person = []
for i in range(0, n):
    person.append(input().split())

person.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(person[-1][0])
print(person[0][0])
