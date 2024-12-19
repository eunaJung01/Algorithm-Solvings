def solution(x, n):
    answer = [x]
    for _ in range(n - 1):
        answer.append(answer[-1] + x)
    return answer
