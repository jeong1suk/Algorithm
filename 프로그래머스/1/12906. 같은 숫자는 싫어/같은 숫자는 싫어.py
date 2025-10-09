def solution(arr):
    answer = []
    
    
    answer.append(arr[0])
    for i in range(1, len(arr)):
        tmp = arr[i-1]
        if tmp != arr[i]:
            answer.append(arr[i])
    return answer