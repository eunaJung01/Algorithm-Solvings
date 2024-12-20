def solution(n):
    answer = 2
    while True:
        if n % answer == 1:
            return answer
        answer += 1
