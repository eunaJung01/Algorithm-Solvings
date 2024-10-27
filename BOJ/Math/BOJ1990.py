# 소수인팰린드롬

import sys
from math import sqrt


# 1. 팰린드롬 찾기
def is_palindrome(x):
    str_x = str(x)
    if str_x == str_x[::-1]:  # [::-1] : 문자열 reverse
        return True
    return False


# 2. 소수인지 확인
def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


a, b = map(int, sys.stdin.readline().split())
if b > 10000000:  # 10000000보다 큰 숫자에서는 팰린드롬인 소수 없음 -> 이 장치가 없으면 시간 초과
    b = 10000000

palindromeList = [num for num in range(a, b + 1) if is_palindrome(num)]
for palindrome in palindromeList:
    if is_prime_number(palindrome):
        print(palindrome)
print(-1)
