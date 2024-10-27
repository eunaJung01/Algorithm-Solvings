# 평균

import sys

input = sys.stdin.readline

N = int(input().strip())
scores = list(map(int, input().split()))

max_score = max(scores)
for i, score in enumerate(scores):
    scores[i] = score / max_score * 100

print(sum(scores) / len(scores))
