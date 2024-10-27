# 진법 변환

N, B = input().split(" ")  # B진법 수 N

numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

for i in range(len(N)):
    result += (int(B) ** (len(N) - 1 - i)) * int(numbers.index(N[i]))

print(result)
