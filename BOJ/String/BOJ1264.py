# 모음의 개수

import sys

input = sys.stdin.readline

line = []
while True:
    temp = input().strip()
    if temp != "#":
        line.append(temp)
    else:
        break

result = []
for l in line:
    r = 0
    for alpha in l:
        if alpha in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            r += 1
    result.append(r)

for r in result:
    print(r)
