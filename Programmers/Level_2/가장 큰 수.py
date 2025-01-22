from functools import cmp_to_key


def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=cmp_to_key(compare))

    answer = ''.join(numbers_str)
    if answer[0] == '0':
        return '0'
    return answer


def compare(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1
    if s1 + s2 < s2 + s1:
        return 1
    return 0


print(solution([979, 97, 978, 81, 818, 817]))
