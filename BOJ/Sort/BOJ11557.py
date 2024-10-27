# Yangjojang of The Year

import sys

input = sys.stdin.readline

T = int(input().strip())
result = []

for _ in range(T):
    schoolNum = int(input().strip())
    school, alcohol = "", int(-1)
    for _ in range(schoolNum):
        s, a = map(str, input().split())
        if int(a) > alcohol:
            school, alcohol = s, int(a)
    result.append(school)

for r in result:
    print(r)
