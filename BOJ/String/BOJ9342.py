# 염색체

alpha = "ABCDEF"
check = "AFC"

num = int(input())

for _ in range(num):
    chro = input()
    chro = ''.join(dict.fromkeys(chro))  # 중복 제거
    result = True  # True : Infected / False : Good

    if chro[0] not in alpha or chro[len(chro) - 1] not in alpha:
        result = False

    if check not in chro:
        result = False

    if result:
        print("Infected!")
    else:
        print("Good")
