# A → B

import sys

A, B = map(str, sys.stdin.readline().split())
B = list(B)

result = 1
while True:
    if int(A) > int(''.join(B)):  # 만들 수 없는 경우
        result = -1
        break
    elif A == ''.join(B):  # 만든 경우
        break
    else:
        if B[len(B) - 1] == '1':  # 맨 끝 숫자가 1이면 제거
            B.pop()
        elif int(B[len(B) - 1]) % 2 == 0:  # 맨 끝 숫자가 짝수면 2로 나누기
            B = list(str(int(int(''.join(B)) / 2)))
        else:  # 그 외의 숫자 : 만들 수 없음
            result = -1
            break
        result += 1
print(result)
