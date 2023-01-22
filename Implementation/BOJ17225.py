# 세훈이의 선물가게

import heapq

blue, red, n = map(int, input().split())

queue = list()
heapq.heapify(queue)
r_end = b_end = 0

for i in range(n):
    time, color, cnt = map(str, input().split())
    time = int(time)
    cnt = int(cnt)
    j = 0
    if color == 'R' and r_end > time:
        time = r_end
    elif color == 'B' and b_end > time:
        time = b_end

    while j < cnt:
        if color == 'B':
            heapq.heappush(queue, (time + blue * j, 'B'))
        else:
            heapq.heappush(queue, (time + red * j, 'R'))
        j += 1

    if color == 'B':
        b_end = time + blue * j
    else:
        r_end = time + red * j

b = list()
r = list()
for j in range(len(queue)):
    popped = heapq.heappop(queue)
    if popped[1] == 'B':
        b.append(j + 1)
    else:
        r.append(j + 1)

print(len(b))
for a in b:
    print(str(a) + " ", end="")
print()
print(len(r))
for d in r:
    print(str(d) + " ", end="")
