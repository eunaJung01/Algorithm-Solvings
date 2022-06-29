# 후위 표기식2

import sys

N = int(sys.stdin.readline())
F = sys.stdin.readline().strip()  # 후위 표기식

numList = []
for _ in range(N):
    numList.append(int(sys.stdin.readline()))

stack = []

for f in F:
    if f == "+":
        stack.append(stack.pop() + stack.pop())
    elif f == "-":
        first = stack.pop()
        second = stack.pop()
        stack.append(second - first)
    elif f == "/":
        first = stack.pop()
        second = stack.pop()
        stack.append(second / first)
    elif f == "*":
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(numList[ord(f) - 65])  # 'A' ascii code = 65

print("%.2f" % stack[0])
