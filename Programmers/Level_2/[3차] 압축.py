def solution(msg):
    dictionary = dict()
    for i in range(26):
        alpha = chr(65 + i)
        dictionary[alpha] = i + 1

    answer = [0]
    last_index = 26
    s = ""

    for i in range(len(msg)):
        s += msg[i]

        if s in dictionary:
            answer[-1] = dictionary[s]
            continue

        last_index += 1
        dictionary[s] = last_index
        s = msg[i]
        answer.append(dictionary[s])

    return answer
