# 한수

import sys

N = int(sys.stdin.readline().strip())

cnt = 0
for i in range(1, N + 1):
    if i < 100:
        cnt += 1
        continue
    nums = list(map(int, str(i)))
    if nums[0] - nums[1] == nums[1] - nums[2]:
        cnt += 1
print(cnt)
