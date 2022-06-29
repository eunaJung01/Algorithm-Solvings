# 소인수분해

N = int(input())

if N != 1:
    i = 2
    while True:
        if N % i == 0:
            print(i)
            N //= i
        else:
            i += 1

        if N == 1:
            break
