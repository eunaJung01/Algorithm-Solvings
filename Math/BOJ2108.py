# 통계학

import sys

N = int(sys.stdin.readline().strip())
num = []
dic = {}

for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
    num.append(n)
num.sort()

av = round(sum(num) / N)  # 산술 평균
mid = num[N // 2]  # 중앙값
range = num[N - 1] - num[0]  # 범위

sorted_dic = sorted(dic.items(), key=lambda items: items[1], reverse=True)
v = sorted_dic[0][1]
i = 0
bin_list = []
while v == sorted_dic[i][1]:
    bin_list.append(sorted_dic[i][0])
    i += 1
    if i >= len(sorted_dic):
        break

bin = 0  # 최빈값
if len(bin_list) == 1:
    bin = bin_list[0]
else:
    bin_list.sort()
    bin = bin_list[1]

print(av)
print(mid)
print(bin)
print(range)
