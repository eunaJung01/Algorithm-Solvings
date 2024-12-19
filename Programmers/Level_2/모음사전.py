n = 5
alphas = ['A', 'E', 'I', 'O', 'U']

weight = [0, 0, 0, 0, 1]
for i in range(1, n):
    weight_idx = n - i - 1
    weight[weight_idx] = weight[weight_idx + 1] + n ** i


def solution(word):
    answer = 0
    for idx, w in enumerate(word):
        answer += weight[idx] * alphas.index(w) + 1
    return answer
