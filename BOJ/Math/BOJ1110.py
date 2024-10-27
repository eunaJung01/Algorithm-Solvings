# 더하기 사이클

num = input()

if len(num) == 1:
    num = '0' + num

cycle = 0
new_num = num
while True:
    new_num = new_num[1] + str(int(new_num[0]) + int(new_num[1]))[-1]
    cycle += 1
    if num == new_num:
        break

print(cycle)
