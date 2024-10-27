# 후위 표기식

# 틀렸습니다 (3%)

# import sys
#
# input = sys.stdin.readline
#
# middle = input().strip()
#
# idx = 0
# postfix = []
# func_stack = []
#
# depth = 0
# while True:
#     if idx >= len(middle):
#         break
#     n = middle[idx]
#
#     if n == "(":
#         pass
#     elif n == ")":
#         if func_stack:
#             postfix.append(func_stack.pop())
#         while func_stack and (func_stack[-1] == "*" or func_stack[-1] == "/"):
#             postfix.append(func_stack.pop())
#     elif n == "*" or n == "/":
#         idx += 1
#         if middle[idx] == "(":
#             func_stack.append(n)
#         else:
#             postfix.append(middle[idx])
#             postfix.append(n)
#     elif n == "+" or n == "-":
#         if func_stack and (func_stack[-1] == "+" or func_stack[-1] == "-"):
#             postfix.append(func_stack.pop())
#         func_stack.append(n)
#     else:
#         postfix.append(n)
#     idx += 1
#
# while func_stack:
#     postfix.append(func_stack.pop())
# print(''.join(postfix))

# ---

import sys

input = sys.stdin.readline

middle = input().strip()

operand_dict = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}  # 연산자 우선 순위
postfix, stack = [], []

for n in middle:
    if "A" <= n <= "Z":
        postfix.append(n)
    elif n == "(":
        stack.append(n)
    elif n == ")":
        while stack and stack[-1] != "(":
            postfix.append(stack.pop())
        stack.pop()  # "("
    else:  # 연산자일 경우
        while stack and operand_dict[n] <= operand_dict[stack[-1]]:
            postfix.append(stack.pop())
        stack.append(n)

while stack:
    postfix.append(stack.pop())

print(''.join(postfix))
