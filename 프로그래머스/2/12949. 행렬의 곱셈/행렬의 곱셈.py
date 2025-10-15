def solution(arr1, arr2):
    row1, column1 = len(arr1), len(arr1[0])
    row2, column2 = len(arr2), len(arr2[0])
    # print(row1, column1)
    # print(row2, column2)
    answer = [[0 for _ in range(column2)] for _ in range(row1)]
    for i in range(row1):
        for j in range(column2):
            for k in range(column1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                # print(f"i={i}, j={j}, k={k}")
    return answer
'''
arr1(0,0) * arr2(0,0) + arr1(0,1) arr2(1,0) / arr1(0,0) * arr2(0,1) + arr1(0,1) + arr2(1,1)
arr1(1,0) * arr2(0,0) + arr1(1,1) arr2(1,0)
arr1(2,0) * arr2(0,0) + arr1(2,1) arr2(1,0)
'''