# 파일 정리

N = int(input())
dct = {}

file_ext = {}
for _ in range(N):
    _, ext = input().split(".")
    if dct.get(ext):
        dct[ext] = dct[ext] + 1
    else:
        dct[ext] = 1

for key, val in sorted(dct.items()):
    print(str(key) + " " + str(val))
