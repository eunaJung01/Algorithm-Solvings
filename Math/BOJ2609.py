# 최대공약수와 최소공배수

# pypy -> 런타임 에러 / python3 -> 성공 (???)
from math import gcd
from math import lcm

num1, num2 = map(int, input().split())

print(gcd(num1, num2))
print(lcm(num1, num2))
