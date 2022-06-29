# 쇠막대기

import sys

line = sys.stdin.readline()

stack = []  # 막대 스택
before = ""
count = 0

for i in line:
    if i == "(":
        stack.append(True)
    elif i == ")":
        if before == "(":  # 레이저
            if len(stack) != 1:
                stack.pop()
                count += len(stack)
            else:  # 잘리는 막대가 없을 경우
                stack.pop()
        else:  # 막대 끝
            count += 1
            stack.pop()
    else:
        continue
    before = i

print(count)
