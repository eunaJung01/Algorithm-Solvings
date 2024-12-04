def solution(s):
    s = s.strip('{}').split('},{')
    s = [list(map(int, group.split(','))) for group in s]

    s_sorted_by_len = sorted(s, key=lambda x: len(x))

    answer = []
    for group in s_sorted_by_len:
        for num in group:
            if num not in answer:
                answer.append(num)
    return answer
