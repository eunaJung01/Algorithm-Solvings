from copy import deepcopy


def solution(want, number, discount):
    arr = []
    i = 0
    for something in discount:
        if i == 0:
            d = dict()
            d[something] = 1
        else:
            d = deepcopy(arr[i - 1])
            if something in d:
                d[something] += 1
            else:
                d[something] = 1
        arr.append(d)
        i += 1

    answer = 0
    left = -1
    right = 9

    while right < len(discount):
        if isAble(want, number, arr, left, right):
            answer += 1
        left += 1
        right += 1

    return answer


def isAble(want, number, arr, left, right):
    for i, w in enumerate(want):

        if w not in arr[right]:
            return False
        right_w_num = arr[right][w]

        if left == -1 or w not in arr[left]:
            left_w_num = 0
        else:
            left_w_num = arr[left][w]

        if right_w_num - left_w_num != number[i]:
            return False
    return True
