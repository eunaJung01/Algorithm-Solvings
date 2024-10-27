alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_num = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
S = input()

numList = []
for s in S:
    numList.append(alpha_num[alpha.index(s)])

while len(numList) != 1:
    temp = []
    idx = 0
    for i in range(int(len(numList) / 2)):
        num = numList[idx] + numList[idx + 1]
        if len(str(num)) == 1:
            temp.append(num)
        else:
            temp.append(int(str(num)[1]))
        idx += 2
    if len(numList) % 2 != 0:
        temp.append(numList[len(numList) - 1])
    numList = temp

if numList[0] % 2 != 0:
    print("I'm a winner!")
else:
    print("You're the winner?")
