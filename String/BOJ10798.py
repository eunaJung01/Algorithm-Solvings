# 세로읽기

s_list = []

for i in range(5):
    s_list.append(input())

for i in range(max(len(s) for s in s_list)):
    for j in range(5):
        if i < len(s_list[j]):
            print(s_list[j][i], end="")
