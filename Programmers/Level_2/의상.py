def solution(clothes):
    cloth_cnt = dict()
    for cloth, cloth_type in clothes:
        if cloth_type in cloth_cnt:
            cloth_cnt[cloth_type] += 1
            continue
        cloth_cnt[cloth_type] = 1

    answer = 1
    for cnt in cloth_cnt.values():
        answer *= cnt + 1
    return answer - 1
