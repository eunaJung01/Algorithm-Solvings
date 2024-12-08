from copy import deepcopy


def solution(str1, str2):
    str1_pairs = get_str_pairs(str1.lower())
    str2_pairs = get_str_pairs(str2.lower())

    if len(str1_pairs) == 0 and len(str2_pairs) == 0:
        return 65536

    intersection_result = intersection(deepcopy(str1_pairs), deepcopy(str2_pairs))
    union_result = union(intersection_result, str1_pairs, str2_pairs)

    return int((len(intersection_result) /
                len(union_result)
                ) * 65536)


def intersection(a1, a2):
    result = []
    for a in a1:
        if a not in a2:
            continue
        a2.remove(a)
        result.append(a)
    return result


def union(intersection_result, a1, a2):
    result = []

    temp = deepcopy(intersection_result)
    for a in a1:
        if a in temp:
            temp.remove(a)
            continue
        result.append(a)

    temp = deepcopy(intersection_result)
    for a in a2:
        if a in temp:
            temp.remove(a)
            continue
        result.append(a)

    result.extend(intersection_result)
    return result


def get_str_pairs(s):
    pairs = []
    for i in range(len(s) - 1):
        if s[i] == " " or s[i + 1] == " ":
            continue
        if 97 <= ord(s[i]) <= 122 and 97 <= ord(s[i + 1]) <= 122:
            pairs.append(s[i:i + 2])
    return pairs
