# 펠린드롬수

import sys

input = sys.stdin.readline

lines = []
while True:
    line = input().strip()
    if line == "0":
        break
    lines.append(line)


def isPNum(num):
    if len(num) % 2 == 0:
        if num[:len(num) // 2] == num[len(num) // 2:][::-1]:
            return True
        else:
            return False
    else:
        if num[:len(num) // 2] == num[len(num) // 2 + 1:][::-1]:
            return True
        else:
            return False


result = []
for line in lines:
    if isPNum(line):
        result.append("yes")
    else:
        result.append("no")

for r in result:
    print(r)
