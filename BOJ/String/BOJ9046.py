# 복호화

T = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"


def get_max_alphabet(sentence):
    count = [0] * 26
    for alpha in sentence:
        count[alphabet.index(alpha)] += 1
    max_idx = count.index(max(count))

    if sorted(count, reverse=True)[1] == max(count):
        print("?")
    else:
        print(alphabet[max_idx])


s_list = []
for i in range(T):
    s_list.append(input().replace(" ", ""))

for s in s_list:
    get_max_alphabet(s)
