# !밀비 급일

sentence_list = []

sentence = input()
while sentence != "END":
    sentence_list.append(sentence)
    sentence = input()

for i in sentence_list:
    print(i[::-1])