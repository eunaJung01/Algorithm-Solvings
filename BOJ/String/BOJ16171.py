# 나는 친구가 적다 (Small)

# 정규식 사용
# import re
#
# line = input()
# regrex = re.compile("[^0-9]")
# line = "".join(regrex.findall(line))
# keyword = input()
#
# if keyword in line:
#     print(1)
# else:
#     print(0)

# ---
line = input()
keyword = input()

line_alpha = ""
num = "0123456789"
for l in line:
    if l not in num:
        line_alpha = line_alpha + l

if keyword in line_alpha:
    print(1)
else:
    print(0)
