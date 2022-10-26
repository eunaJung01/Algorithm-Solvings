# 약수의 합 2

# 시간초과 예상
# import sys
#
# input = sys.stdin.readline
#
# N = int(input().strip())
#
# result = 0
# for n in range(1, N + 1):
#     result += n
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             result += i
# print(result)

# ---

N = int(input())
print(sum(i * (N // i) for i in range(1, N + 1)))
