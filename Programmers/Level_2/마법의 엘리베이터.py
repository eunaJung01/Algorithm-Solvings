def solution(storey):
    storey = list(map(int, str(storey)))

    answer = 0
    while storey:
        n = storey.pop()

        if n < 5:
            answer += n
            continue
        if n == 5 and ((len(storey) > 0 and storey[-1] < 5) or len(storey) == 0):
            answer += n
            continue

        answer += 10 - n
        if len(storey) == 0:
            answer += 1
            continue
        storey.append(storey.pop() + 1)

    return answer
