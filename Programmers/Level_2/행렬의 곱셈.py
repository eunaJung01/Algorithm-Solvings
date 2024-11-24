def solution(arr1, arr2):
    arr1_n = len(arr1)
    arr1_m = len(arr1[0])
    arr2_m = len(arr2[0])

    answer = [[0 for _ in range(arr2_m)] for _ in range(arr1_n)]

    for arr1_y in range(arr1_n):
        for arr2_x in range(arr2_m):
            for i in range(arr1_m):
                answer[arr1_y][arr2_x] += arr1[arr1_y][i] * arr2[i][arr2_x]
    return answer
