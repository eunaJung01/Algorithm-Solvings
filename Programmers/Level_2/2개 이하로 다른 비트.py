def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(number))
    return answer


def f(x):
    if x % 2 == 0:
        return x + 1

    # 1. 가장 낮은 0을 1로 변경
    # 2. 그 뒤에 있는 1을 0으로 변경
    bit_mask = 1
    while x & bit_mask:
        bit_mask <<= 1
    return x + bit_mask - (bit_mask >> 1)
