# 단어 공부

import sys

word = sys.stdin.readline().strip()

dic = {}
for w in word:
    check = w.upper()
    if check in dic:
        dic[check] += 1
    else:
        dic[check] = 1

sorted_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)

result = sorted_dic[0][0]
for i in range(1, len(sorted_dic)):
    if sorted_dic[0][1] == sorted_dic[i][1]:
        result = "?"
        break

print(result)
