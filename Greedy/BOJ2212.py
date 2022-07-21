# 센서

import sys

N = int(sys.stdin.readline().strip())  # 센서의 개수
K = int(sys.stdin.readline().strip())  # 집중국의 개수
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()

d = []
for i in range(N - 1):
    d.append(sensor[i + 1] - sensor[i])
d.sort()

result = 0
for i in range(N - K):
    result += d[i]
print(result)
