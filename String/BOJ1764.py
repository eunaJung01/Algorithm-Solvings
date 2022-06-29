# 듣보잡

# 시간 초과..
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# N_list = []
# result = []
#
# for _ in range(N):
#     N_list.append(input())
# for _ in range(M):
#     line = input()
#     if line in N_list:
#         result.append(line)
#
# result.sort()
#
# print(len(result))
# for r in result:
#     print(r)

# set.intersection
import sys

N, M = map(int, sys.stdin.readline().split())
N_set = set()
M_set = set()

for _ in range(N):
    N_set.add(input())
for _ in range(M):
    M_set.add(input())

result = list(N_set.intersection(M_set))
result.sort()

print(len(result))
for r in result:
    print(r)
