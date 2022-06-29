# 단어 뒤집기 2

line = input()

result = ""
reverse = ""

i = 0
while True:
    if i == len(line):
        break

    if line[i] == "<":
        while line[i] != ">":
            result += line[i]
            i += 1
        result += line[i]  # ">"
        i += 1
    elif line[i] == " ":
        result += line[i]
        i += 1
    else:
        while i != len(line) and line[i] != "<" and line[i] != " ":
            reverse += line[i]
            i += 1
        result += reverse[::-1]
        reverse = ""

print(result)
