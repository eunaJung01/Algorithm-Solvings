# 단어 수학

# import sys
# import heapq
#
# input = sys.stdin.readline
#
# N = int(input().strip())
#
# max_len = 8
# vocabs = [[-1 for _ in range(max_len + 1)] for _ in range(N)]
# for y in range(N):
#     voc = input().strip()[::-1]
#     for i, v in enumerate(voc):
#         vocabs[y][max_len - i] = ord(v) - 65
#
# # A: 65, Z: 90 -> ord()
# alpha_a = [[0, i] for i in range(26)]
# for j in range(max_len + 1):
#     a = 10 ** (max_len + 1 - j)  # 가중치
#     for i in range(N):
#         if vocabs[i][j] == -1:
#             continue
#         alpha_a[vocabs[i][j]][0] -= a
#
# heapq.heapify(alpha_a)
# alpha = [-1 for i in range(26)]
# max_num = 9
# while max_num >= 0 and alpha_a:
#     _, idx = heapq.heappop(alpha_a)
#     alpha[idx] = max_num
#     max_num -= 1
#
# result = 0
# for i in range(N):
#     j = max_len
#     num = ""
#     while j >= 0 and vocabs[i][j] != -1:
#         num = str(alpha[vocabs[i][j]]) + num
#         j -= 1
#     result += int(num)
# print(result)

import sys

input = sys.stdin.readline

N = int(input())
vocabs = [input().strip() for _ in range(N)]

alphas = [0 for _ in range(26)]
for voc in vocabs:
    for i, v in enumerate(voc):
        alphas[ord(v) - 65] += 10 ** (len(voc) - i - 1)
alphas.sort(reverse=True)

result, max_num = 0, 9
for i in alphas:
    result += max_num * i
    max_num -= 1
print(result)
