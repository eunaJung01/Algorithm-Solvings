def solution(gems):
    answer = [0, 0]
    start = 0
    gem_rightmost_idx = dict()

    for end in range(len(gems)):
        if gems[end] not in gem_rightmost_idx:
            gem_rightmost_idx[gems[end]] = end
            answer = [start + 1, end + 1]
            continue

        gem_rightmost_idx[gems[end]] = end

        if gems[start] == gems[end]:
            start = get_min_rightmost_idx(gem_rightmost_idx)
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]

    return answer


def get_min_rightmost_idx(gem_rightmost_idx):
    idx = int(1e9)
    for i in gem_rightmost_idx.values():
        idx = min(idx, i)
    return idx
