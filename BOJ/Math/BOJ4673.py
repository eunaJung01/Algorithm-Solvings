# 셀프 넘버

isSelfNumber = [True for _ in range(10000 + 1)]

for number in range(1, 10000 + 1):
    s = number
    for n in str(number):
        s += int(n)
    if s <= 10000:
        isSelfNumber[s] = False

for number in range(1, 10000 + 1):
    if isSelfNumber[number]:
        print(number)
