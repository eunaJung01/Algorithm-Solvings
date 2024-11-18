def solution(elements):
    n = len(elements)

    sums = [0] * (n * 2 - 1)
    sums[0] = elements[0]

    answer = set()
    for i in range(n):
        answer.add(elements[i])

    for i in range(1, len(sums)):
        sums[i] = sums[i - 1] + elements[i % n]
    answer.add(sums[n - 1])

    for partial_len in range(2, n):
        for start in range(n):
            end = start + partial_len - 1
            p = end - partial_len

            if p == -1:
                answer.add(sums[end])
                continue
            answer.add(sums[end] - sums[p])

    return len(answer)
