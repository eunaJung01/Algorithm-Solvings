def solution(num):
    answer = 0

    while num != 1:
        answer += 1
        if answer == 500:
            return -1

        if num % 2 == 0:
            num //= 2
            continue
        num *= 3
        num += 1

    return answer
