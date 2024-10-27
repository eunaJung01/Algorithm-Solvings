# 폰 호석만

# 부분 성공 (19/24)
"""
num_A, num_B = input().split()
numbers = "0123456789abcdefghijklmnopqrstuvwxyz"

X, A, B = 0, 0, 0
count = 0

for i in range(2, 37):  # A진법
    for j in range(2, 37):  # B진법
        ten_A = 0
        ten_B = 0
        A_idx_reverse = -1
        B_idx_reverse = -1
        numbers_A = []
        numbers_B = []

        for A_idx in range(len(num_A)):
            number = int(numbers.index(num_A[A_idx_reverse]))
            ten_A += (i ** A_idx) * number
            A_idx_reverse -= 1

            if number <= i:
                numbers_A.append(number)

        for B_idx in range(len(num_B)):
            number = int(numbers.index(num_B[B_idx_reverse]))
            ten_B += (j ** B_idx) * number
            B_idx_reverse -= 1

            if number <= j:
                numbers_B.append(number)

        if ten_A == ten_B and i != j and len(numbers_A) != 0 and len(numbers_B) != 0:
            X = ten_A
            A = i
            B = j
            count += 1

if count == 0 or X >= 2 ** 63:
    print("Impossible")
elif count >= 2:
    print("Multiple")
else:
    print(X, A, B)
"""

# 성공
num_A, num_B = input().split()
numbers = "0123456789abcdefghijklmnopqrstuvwxyz"

X, A, B = 0, 0, 0
count = 0

numbers_A = []
numbers_B = []

for a in num_A:
    numbers_A.append(int(numbers.index(a)))
for b in num_A:
    numbers_B.append(int(numbers.index(b)))

for i in range(2, 37):
    try:
        ten_A = int(num_A, i)
    except:
        continue

    for j in range(2, 37):
        try:
            ten_B = int(num_B, j)

            for number_A in numbers_A:
                if number_A > i:
                    numbers_A.remove(number_A)
            for number_B in numbers_B:
                if number_B > j:
                    numbers_B.remove(number_B)

            if ten_A == ten_B and i != j and len(numbers_A) != 0 and len(numbers_B) != 0:
                X = ten_A
                A = i
                B = j
                count += 1

        except:
            continue

if count == 0 or X >= 2 ** 63:
    print("Impossible")
elif count >= 2:
    print("Multiple")
else:
    print(X, A, B)
