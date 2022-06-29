# 비밀번호 발음하기

# vowel = ['a', 'e', 'i', 'o', 'u']
vowel = "aeiou"

while True:
    result = True
    has_vowel = False  # 모음 존재 여부
    vowel_count = 0  # 연속 모음 개수
    consonant_count = 0  # 연속 자음 개수
    alpha_count = 1  # 연속 글자

    str = input()
    if str == "end":
        break

    alpha = str[0]
    if alpha in vowel:
        has_vowel = True
        vowel_count = vowel_count + 1
    else:
        consonant_count = consonant_count + 1

    for i in range(1, len(str)):
        if alpha == str[i]:
            alpha_count = alpha_count + 1
            if (alpha_count == 2 and alpha != 'e' and alpha != 'o') or (alpha_count == 3):
                result = False
                break
        else:
            alpha_count = 1
        alpha = str[i]

        if alpha in vowel:
            has_vowel = True
            vowel_count = vowel_count + 1
            if vowel_count == 3:
                result = False
                break
            if consonant_count != 0:
                consonant_count = 0

        else:
            consonant_count = consonant_count + 1
            if consonant_count == 3:
                result = False
                break
            if vowel_count != 0:
                vowel_count = 0

    if not has_vowel or not result:
        print("<" + str + ">" + " is not acceptable.")
    else:
        print("<" + str + ">" + " is acceptable.")
