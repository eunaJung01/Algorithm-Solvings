# 스택
import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    line = sys.stdin.readline().split()
    inst = line[0]
    # --- 시간 초과 ---
    # inst = input()

    # if inst[:4] == "push":
    #     stack.append(inst[5:])
    # ---
    if inst == "push":
        stack.append(line[1])

    elif inst == "pop":
        if len(stack) != 0:
            print(stack.pop(-1))
        else:
            print(-1)

    elif inst == "size":
        print(len(stack))

    elif inst == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)

    elif inst == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

    else:
        break
