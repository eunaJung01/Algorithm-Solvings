from collections import deque


def solution(number, k):
    total_number_cnt = len(number)
    numbers = deque([int(i) for i in number])

    answer = [numbers.popleft()]
    pop_cnt = 0
    while numbers and pop_cnt < k:
        number = numbers.popleft()
        while (len(answer) > 0 and
               answer[-1] < number and
               pop_cnt < k):
            answer.pop()
            pop_cnt += 1
        answer.append(number)

    while numbers:
        answer.append(numbers.popleft())

    while len(answer) > total_number_cnt - k:
        answer.pop()
    return ''.join([str(i) for i in answer])
