# 대소문자 바꾸기

import sys

line = sys.stdin.readline().strip()

result = ""
for l in line:
    if l.isupper():
        result += l.lower()
    else:
        result += l.upper()
print(result)
