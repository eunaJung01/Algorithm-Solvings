def solution(sequence):
    for i in range(0, len(sequence), 2):
        sequence[i] *= -1
    answer = find(sequence)

    for i in range(len(sequence)):
        sequence[i] *= -1
    answer = max(answer, find(sequence))
    return answer


def find(sequence):
    max_sum = [0 for _ in range(len(sequence))]
    max_sum[0] = sequence[0]

    for i in range(1, len(sequence)):
        max_sum[i] = max(max_sum[i - 1] + sequence[i], sequence[i])
    return max(max_sum)
