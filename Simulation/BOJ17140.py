# 이차원 배열과 연산

import sys
import heapq

r, c, k = map(int, sys.stdin.readline().split())
N, M = 3, 3  # N : 행 개수 / M : 열 개수

A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))


# 수 커지는 순으로 정렬 / 0 제외
def get_sorted_line(dic):
    line = []
    q = []  # 우선 순위 큐
    count = 0  # key 개수 (0 제외)

    for key, value in dic:
        if key != 0:
            count += 1

            # 다른 value일 경우 전부 pop
            if len(q) != 0 and q[0][0] != value:
                while q:
                    t = heapq.heappop(q)
                    line.append(t[1])
                    line.append(t[0])
                heapq.heappush(q, (value, key))

            # 같은 value일 경우 push
            else:
                heapq.heappush(q, (value, key))
                heapq.heapify(q)

    while q:
        t = heapq.heappop(q)
        line.append(t[1])
        line.append(t[0])

    return count, line


# 행에 대한 정렬
def R():
    global M
    m = 0

    for y in range(N):
        dic = {}  # key : 수 / value: 수 등장 횟수

        for x in range(M):
            if A[y][x] in dic:
                dic[A[y][x]] += 1
            else:
                dic[A[y][x]] = 1

        # 수 등장 횟수가 커지는 순으로 정렬
        sorted_dic = sorted(dic.items(), key=lambda item: item[1])

        # 수 커지는 순으로 정렬 / 0 제외
        count, line = get_sorted_line(sorted_dic)

        A[y] = line  # 헹 변경
        m = max(m, 2 * count)

    # 열의 크기가 100을 넘어가는 경우
    if m > 100:
        m = 100

    if M < m:
        M = m

    # 0 채우기
    for y in range(N):
        for i in range(M - len(A[y])):
            A[y].append(0)


# 열에 대한 정렬
def C():
    global N
    n = 0
    col = []

    for x in range(M):
        dic = {}

        for y in range(N):
            if A[y][x] in dic:
                dic[A[y][x]] += 1
            else:
                dic[A[y][x]] = 1

        # 수 등장 횟수가 커지는 순으로 정렬
        sorted_dic = sorted(dic.items(), key=lambda item: item[1])

        # 수 커지는 순으로 정렬 / 0 제외
        count, line = get_sorted_line(sorted_dic)
        col.append(line)
        n = max(n, 2 * count)

    # 행의 크기가 100을 넘어가는 경우
    if n > 100:
        n = 100

    if N < n:
        for _ in range(n - N):
            A.append([0 for _ in range(M)])
        N = n

    for x in range(M):
        for y in range(N):
            if y < len(col[x]):
                A[y][x] = col[x][y]  # 값 변경
            else:  # 0 채우기
                A[y][x] = 0


r -= 1
c -= 1
time = 0

while True:
    if len(A) > r and len(A[0]) > c:  # 범위 확인 (런타임 에러 - Index error 발생)
        if A[r][c] == k:
            break

    if time == 100:
        time = -1
        break

    if N >= M:  # R 연산
        R()
    else:  # C 연산
        C()

    time += 1

print(time)
