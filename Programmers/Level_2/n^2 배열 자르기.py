def solution(n, left, right):
    answer = []
    for num in range(left, right + 1):
        y = num // n
        x = num % n
        answer.append(max(y, x) + 1)
    return answer
