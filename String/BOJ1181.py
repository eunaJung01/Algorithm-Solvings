# 단어 정렬

N = int(input())
lst = []

for _ in range(N):
    str = input()
    if str not in lst:
        lst.append(str)

lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)
