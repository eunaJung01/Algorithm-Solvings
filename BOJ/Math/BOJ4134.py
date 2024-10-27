# 다음 소수

from math import sqrt


def is_prime_number(x):
    if x == 0 or x == 1:  # x == 0 조건 없으면 틀렸다고 뜸
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


n = int(input())
numList = []
for _ in range(n):
    numList.append(int(input()))

for j in numList:
    while True:
        if is_prime_number(j):
            print(j)
            break
        else:
            j += 1
