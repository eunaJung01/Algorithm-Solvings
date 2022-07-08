# 마법사 상어와 파이어볼

import sys

N, M, K = map(int, sys.stdin.readline().split())  # NxN 격자 / M개의 파이어볼

grid = [[[] for _ in range(N)] for _ in range(N)]  # 파이어볼 번호 리스트

fireball = []  # 위치(r, c), 질량 m, 속력 s, 방향 d
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    temp[0] -= 1
    temp[1] -= 1
    fireball.append(temp)

dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)
d_list = [(0, 2, 4, 6), (1, 3, 5, 7)]  # 모두 짝수 또는 홀수 / 그 외


def move():
    for i in range(len(fireball)):
        r, c, m, s, d = fireball[i]
        grid[(r + dy[d] * s) % N][(c + dx[d] * s) % N].append(i)


def reset_fireball():
    global grid
    new = []  # new fireball list

    for y in range(N):
        for x in range(N):
            # 파이어볼 1개 존재하는 경우
            if len(grid[y][x]) == 1:
                r, c, m, s, d = fireball[grid[y][x][0]]
                new.append([y, x, m, s, d])

            # 파이어볼 존재하지 않는 경우
            elif len(grid[y][x]) == 0:
                continue

            # 파이어볼 2개 이상 존재하는 경우
            else:
                m, s = 0, 0  # 질량, 속력
                d_status = 0 if fireball[grid[y][x][0]][4] % 2 == 0 else 1  # 짝수일 경우 0 / 홀수일 경우 1
                d_idx = 0  # d_list 인덱스

                for idx in grid[y][x]:
                    m += fireball[idx][2]
                    s += fireball[idx][3]
                    d_temp = 0 if fireball[idx][4] % 2 == 0 else 1  # 짝수일 경우 0 / 홀수일 경우 1
                    if d_temp != d_status:
                        d_idx = 1

                m //= 5  # ⌊(합쳐진 파이어볼 질량의 합)/5⌋
                if m == 0:  # 질량이 0인 파이어볼은 소멸
                    grid[y][x] = []  # 초기화
                    continue

                s //= len(grid[y][x])  # ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋

                for i in range(4):
                    new.append([y, x, m, s, d_list[d_idx][i]])

            grid[y][x] = []  # 초기화

    return new


for _ in range(K):
    move()  # 이동
    fireball = reset_fireball()  # 연산

result = 0
for f in fireball:
    result += f[2]
print(result)
