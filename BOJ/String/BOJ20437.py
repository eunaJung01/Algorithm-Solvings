# 문자열 게임2

import sys

T = int(sys.stdin.readline().strip())
result = []

for _ in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())

    dic = {}
    idx = 0
    for w in W:
        if w in dic:
            # 한번에 처리 불가.......
            temp = dic.get(w)
            temp.append(idx)
            dic[w] = temp
        else:
            dic[w] = [idx]
        idx += 1

    lst = []
    for d in dic.values():
        if len(d) >= K:
            lst.append(d)

    if len(lst) == 0:
        result.append(-1)
        continue
    else:
        len_list = []
        for l in lst:
            cur = 0
            while cur + K <= len(l):
                first = l[cur]
                last = l[cur + K - 1]
                len_list.append(last - first + 1)
                cur += 1
        result.append([min(len_list), max(len_list)])

for r in result:
    if r == -1:
        print(r)
    else:
        print(r[0], r[1])
