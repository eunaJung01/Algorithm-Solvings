# 단어 수학

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
