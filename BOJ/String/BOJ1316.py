# 그룹 단어 체커

N = int(input())

count = 0
alpha_list = []

for i in range(N):
    word = input()
    alpha = word[0]
    alpha_list.append(alpha)

    j = 1
    while j < len(word):
        if alpha != word[j]:
            alpha = word[j]
            if alpha in alpha_list:
                alpha_list = []
                break
            else:
                alpha_list.append(alpha)
        j = j + 1

    if len(alpha_list) != 0:
        count = count + 1
    alpha_list = []

print(count)
