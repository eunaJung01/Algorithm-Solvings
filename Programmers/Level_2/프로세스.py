from collections import deque


def solution(priorities, location):
    priorities_i = deque()
    for i, priority in enumerate(priorities):
        priorities_i.append([priority, i])

    answer = 0
    while True:
        p, i = priorities_i.popleft()
        if not is_able_to_run(priorities_i, p):
            priorities_i.append([p, i])
            continue
        answer += 1
        if i == location:
            return answer


def is_able_to_run(priorities_i, p_to_check):
    for p, _ in priorities_i:
        if p_to_check < p:
            return False
    return True
