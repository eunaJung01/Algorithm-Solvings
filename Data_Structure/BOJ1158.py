# 요세푸스 문제

import sys


# shift left -K (pop 되어야 하는 값의 인덱스가 len(queue)-1이 될 때까지)
def shift_left(queue, K):
    temp = []
    for q in range(len(queue)):
        idx = (K + q) % len(queue)
        temp.append(queue[idx])
    return temp


N, K = map(int, sys.stdin.readline().split())
queue = [num for num in range(1, N + 1)]
count = 0

print("<", end='')
while len(queue) != 0:
    queue = shift_left(queue, K)
    print(queue.pop(len(queue) - 1), end='')
    count += 1
    if count != N:
        print(", ", end='')
print(">")
