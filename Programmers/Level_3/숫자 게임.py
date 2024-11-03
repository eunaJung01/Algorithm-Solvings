from collections import deque


def solution(A, B):
    A.sort()
    A = deque(A)
    B.sort()

    answer = 0
    for b in B:
        if b > A[0]:
            answer += 1
            A.popleft()

    return answer
