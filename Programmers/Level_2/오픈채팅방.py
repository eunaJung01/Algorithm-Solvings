def solution(record):
    records = []
    nicknames = dict()
    for r in record:
        operation, left = r.split(" ", 1)
        if operation == "Leave":
            records.append((operation, left))
            continue
        user_id, nickname = left.split(" ")
        records.append((operation, user_id))
        nicknames[user_id] = nickname

    answer = []
    for operation, user_id in records:
        if operation == "Enter":
            answer.append(nicknames[user_id] + "님이 들어왔습니다.")
            continue
        if operation == "Leave":
            answer.append(nicknames[user_id] + "님이 나갔습니다.")
    return answer
