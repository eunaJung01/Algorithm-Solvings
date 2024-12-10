from collections import deque


def solution(numbers, target):
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    answer = 0
    while q:
        total, prev_i = q.popleft()

        i = prev_i + 1
        total_plus = total + numbers[i]
        total_minus = total - numbers[i]

        if i == len(numbers) - 1:
            if total_plus == target:
                answer += 1
            if total_minus == target:
                answer += 1
            continue
        q.append((total_plus, i))
        q.append((total_minus, i))

    return answer
