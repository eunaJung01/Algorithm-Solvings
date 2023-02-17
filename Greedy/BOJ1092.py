# 배

import sys

input = sys.stdin.readline

N = int(input().strip())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input().strip())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
else:
    cnt = 0
    while boxes:
        cnt += 1
        for c in range(len(cranes)):
            for b in range(len(boxes)):
                if cranes[c] >= boxes[b]:
                    boxes.pop(b)
                    break
    print(cnt)
