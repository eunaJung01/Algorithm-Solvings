# 트럭

import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)
time = 0

while trucks:
    bridge.popleft()
    if len(bridge) < w and sum(bridge) + trucks[0] <= L:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
    time += 1

print(time + w)
