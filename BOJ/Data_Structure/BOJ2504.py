# 괄호의 값

import sys
from collections import deque

line = sys.stdin.readline().strip()

stack = []  # (), []
temp = ""  # stack에서 pop한 값

calc_queue = deque()  # 계산해야 하는 값들
calc = 0  # 계산 결과값 -> stack에 push

result = 0

# 올바르지 않은 괄호열 판독
result_status = True
status = False

for l in line:
    # 여는 괄호 -> push
    if l == "(" or l == "[":
        stack.append(l)

    # 닫는 괄호 -> 해당 짝까지 pop
    elif l == ")":
        while temp != "(" and len(stack) > 0:
            temp = stack.pop()
            calc_queue.append(temp)
            if temp == "(":
                status = True

        if not status:  # 해당 짝이 없었다면 종료
            result_status = False
            break
        else:
            status = False

    elif l == "]":
        while temp != "[" and len(stack) > 0:
            temp = stack.pop()
            calc_queue.append(temp)
            if temp == "[":
                status = True

        if not status:  # 해당 짝이 없었다면 종료
            result_status = False
            break
        else:
            status = False

    # 괄호 이외의 입력 시 종료
    else:
        result_status = False
        break

    # 닫힌 괄호 -> calc_stack에 들어간 값 계산 & 결과값을 stack에 push
    if l == ")" or l == "]":
        # calc_stack에 값이 2개 이상 들어간 경우 (괄호가 2개 이상 들어갔다면 종료)
        if len(calc_queue) > 1:
            temp = calc_queue.popleft()  # 첫번째 값

            # 첫번째 값이 숫자인 경우
            if temp != "(" and temp != "[":
                calc += temp
                temp = calc_queue.popleft()  # 두번째 값

                # 2번째 값도 숫자일 경우 -> 숫자끼리 전부 더하고 마지막에 괄호값 곱하기
                if temp != "(" and temp != "[":
                    calc += temp
                    while len(calc_queue) > 1:
                        temp = calc_queue.popleft()
                        calc += temp

                    temp = calc_queue.popleft()  # 괄호만 남은 상황
                    if temp == "(":
                        calc *= 2
                    else:
                        calc *= 3

                # 1번째 값은 숫자, 2번째 값은 괄호인 경우 -> 곱하기 (단, calc_stack에 값이 더 남아 있다면 종료)
                else:
                    if len(calc_queue) == 0:
                        if temp == "(":
                            calc *= 2
                        else:
                            calc *= 3
                    else:
                        result_status = False
                        break

            # calc_stack의 길이가 2 이상, 첫번째 값이 괄호인 경우 -> 종료
            else:
                result_status = False
                break

        # calc_stack에 값이 1개만 들어간 경우 ('(' 또는 '[')
        else:
            temp = calc_queue.popleft()
            if temp == "(":
                calc += 2
            else:
                calc += 3

        # calc_stack 계산 결과값을 stack에 push
        stack.append(calc)

        # 초기화
        calc = 0
        temp = ""

if not result_status:
    print(0)
elif "(" in stack or "[" in stack:
    print(0)
else:
    for s in stack:
        result += s
    print(result)
