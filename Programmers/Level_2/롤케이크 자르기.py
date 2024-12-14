def solution(topping):
    n = len(topping)

    right_dict = dict()
    for t in topping:
        if t in right_dict:
            right_dict[t] += 1
        else:
            right_dict[t] = 1

    answer = 0
    left_dict = dict()
    for t in topping[:n - 1]:
        if t in left_dict:
            left_dict[t] += 1
        else:
            left_dict[t] = 1

        right_dict[t] -= 1
        if right_dict[t] == 0:
            right_dict.pop(t)

        if len(left_dict) == len(right_dict):
            answer += 1
    return answer
