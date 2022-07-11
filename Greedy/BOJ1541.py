# 잃어버린 괄호

import sys

line = sys.stdin.readline().strip()

lst = []
s = []
for l in line:
    if l != '+' and l != '-':
        s.append(l)
    else:
        lst.append(int(''.join(s)))
        lst.append(l)
        s = []
lst.append(int(''.join(s)))

result = 0
stack = []
status = "p"
for l in lst:
    if l == '+':
        continue
    elif l == '-':
        while stack:
            if status == "p":
                result += stack.pop()
            else:
                result -= stack.pop()
        status = "m"
    else:
        stack.append(l)
while stack:
    if status == "p":
        result += stack.pop()
    else:
        result -= stack.pop()

print(result)
