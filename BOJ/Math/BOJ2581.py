# 소수

from math import sqrt

# M 이상 N 이하의 자연수
M = int(input())
N = int(input())


# 소수임을 판별하는 함수
def is_prime_number(x):
    if x == 1:  # !!!!
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


primeNum = []
for j in range(M, N + 1):
    if is_prime_number(j):
        primeNum.append(j)

if len(primeNum) == 0:
    print(-1)
else:
    result = 0
    for j in primeNum:
        result += j
    print(result)
    print(primeNum[0])
