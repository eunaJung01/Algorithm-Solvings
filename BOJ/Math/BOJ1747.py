# 소수&팰린드롬

from math import sqrt


def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for j in range(2, int(sqrt(x)) + 1):
        if x % j == 0:
            return False
    return True


def is_palindrome(x):
    str_x = str(x)
    if str_x == str_x[::-1]:  # [::-1] : 문자열 reverse
        return True
    return False


N = input()

while True:
    # num = int(len(N) / 2)
    # count = 0
    # for i in range(num):
    #     if N[i] == N[-i - 1]:
    #         count += 1
    # if num == count and is_prime_number(int(N)):
    #     print(N)
    #     break
    if is_palindrome(int(N)) and is_prime_number(int(N)):
        print(N)
        break
    else:
        N = str(int(N) + 1)
