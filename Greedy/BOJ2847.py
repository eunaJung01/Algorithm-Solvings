# 게임을 만든 동준이

import sys

input = sys.stdin.readline

N = int(input().strip())
score = [int(input().strip()) for _ in range(N)]

result = 0

# 앞에서부터 돌릴 경우 부분 최적해를 만족하지 못하는 경우 발생
# for i in range(N - 1):
#     cur = score[i]
#     next = score[i + 1]
#     if cur >= next:
#         while cur >= next:
#             cur -= 1
#             result += 1
#             if i > 0 and score[i - 1] >= cur:
#                 while score[i - 1] >= cur:
#                     score[i - 1] -= 1
#                     result += i
#     score[i] = cur

for i in range(len(score) - 1, 0, -1):
    if score[i] > score[i - 1]:
        continue
    else:
        result += score[i - 1] - score[i] + 1
        score[i - 1] = score[i] - 1
print(result)
