def solution(n, s):
    if n > s:
        return [-1]

    answer = [int(s / n)] * n
    remainder = s % n

    i = 0
    while remainder > 0:
        answer[i] += 1
        remainder -= 1
        i += 1

    answer.sort()
    return answer
