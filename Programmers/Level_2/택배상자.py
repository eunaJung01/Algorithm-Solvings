from collections import deque


def solution(order):
    order = deque(order)
    belt = deque([i for i in range(1, len(order) + 1)])
    stack = []

    answer = 0
    while True:
        if len(order) == 0:
            break
        o = order[0]

        if len(stack) > 0 and stack[-1] == o:
            order.popleft()
            stack.pop()
            answer += 1
            continue

        if len(belt) > 0:
            b = belt.popleft()
            if b == o:
                order.popleft()
                answer += 1
                continue
            stack.append(b)
            continue
        break

    return answer
