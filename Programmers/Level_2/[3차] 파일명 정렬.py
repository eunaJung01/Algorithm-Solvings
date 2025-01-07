def solution(files):
    arr = []
    for i, file in enumerate(files):
        head, number = divide_head_and_number(file)
        arr.append((head, number, i, file))
    arr.sort(key=lambda x: (x[0], x[1], x[2]))

    answer = []
    for _, _, _, a in arr:
        answer.append(a)
    return answer


def divide_head_and_number(file):
    number = ""
    number_start_i = 0

    is_number = False
    for i, f in enumerate(file):
        if 48 <= ord(f) <= 57:
            number += f
            if not is_number:
                number_start_i = i
                is_number = True
            continue
        if is_number:
            break

    return file[:number_start_i].lower(), int(number)
