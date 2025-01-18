INF = int(1e9)


def solution(a):
    min_num = min(a)
    min_idx = a.index(min_num)
    answer = 1

    left_max_num = INF
    for i in range(min_idx):
        if left_max_num >= a[i]:
            left_max_num = a[i]
            answer += 1

    right_max_num = INF
    for i in range(len(a) - 1, min_idx, -1):
        if right_max_num >= a[i]:
            right_max_num = a[i]
            answer += 1

    return answer
