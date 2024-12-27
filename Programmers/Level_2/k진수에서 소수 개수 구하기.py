from math import sqrt


def solution(n, k):
    numbers = (convert_notation_ten_to_k(int(n), int(k))
               .split("0"))

    answer = 0
    for num_str in numbers:
        if num_str == '':
            continue
        if is_prime_number(int(num_str)):
            answer += 1
    return answer


def convert_notation_ten_to_k(n, k):
    if k == 10:
        return str(n)

    ret = ""
    while n:
        ret += str(n % k)
        n //= k
    return ret[::-1]


def is_prime_number(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
