from collections import deque


def solution(numbers):
    temp = deque()
    for i, num in enumerate(numbers):
        temp.append((num, i))
    numbers = temp

    answer = [-1 for _ in range(len(numbers))]
    stack = []

    while numbers:
        if len(stack) == 0:
            stack.append(numbers.popleft())
            continue

        while len(stack) > 0 and stack[-1][0] < numbers[0][0]:
            num, i = stack.pop()
            answer[i] = numbers[0][0]
        stack.append(numbers.popleft())

    return answer


print(solution([2, 3, 3, 5]))
