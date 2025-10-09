def solution(A, B):
    A.sort()
    B.sort()
    
    a = b = answer = 0
    n = len(A)
    
    while a < n and b < n:
        if B[b] > A[a]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
    
    return answer
'''
A, B 배열의 크기가 같을 때 B 배열의 숫자가 최대한 더 큰 경우의 수 찾기
A, B 길이 100,000 이하, 각 원소는 1,000,000,000 이하 자연수
'''