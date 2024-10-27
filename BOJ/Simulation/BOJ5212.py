# 지구 온난화

import copy
import sys

R, C = map(int, sys.stdin.readline().split())

m = []
for _ in range(R):
    m.append(list(sys.stdin.readline().strip()))

d_r = (-1, 0, 1, 0)
d_c = (0, 1, 0, -1)

m_new = copy.deepcopy(m)
for r in range(R):
    for c in range(C):
        count = 0
        if m[r][c] == 'X':
            for i in range(4):
                cur_r = r + d_r[i]
                cur_c = c + d_c[i]

                if 0 <= cur_r < R and 0 <= cur_c < C:
                    if m[cur_r][cur_c] == '.':
                        count += 1
                else:
                    count += 1

        if count >= 3:
            m_new[r][c] = '.'

# 지도 크기 조정
while True:  # 행 [0]
    if 'X' not in m_new[0]:
        m_new.pop(0)
    else:
        break

while True:  # 행 [-1]
    if 'X' not in m_new[-1]:
        m_new.pop(-1)
    else:
        break

row_len = len(m_new)
while True:  # 열 [0]
    count = 0
    for r in range(row_len):
        if m_new[r][0] == 'X':
            break
        else:
            count += 1
    if count == row_len:
        for r in range(row_len):
            m_new[r].pop(0)
    else:
        break

while True:  # 열 [-1]
    count = 0
    for r in range(row_len):
        if m_new[r][-1] == 'X':
            break
        else:
            count += 1
    if count == row_len:
        for r in range(row_len):
            m_new[r].pop(-1)
    else:
        break

for r in m_new:
    print(''.join(r))
