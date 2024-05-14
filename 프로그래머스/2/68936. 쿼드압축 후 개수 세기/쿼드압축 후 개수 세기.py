def solution(arr):
    answer = [0,0]
    l = len(arr)
    def compression(a, b, l):
        start = arr[a][b]
        for i in range(a, a+l):
            for j in range(b, b+l):
                if arr[i][j] != start:
                    l = l // 2
                    compression(a, b, l)
                    compression(a+l, b, l)
                    compression(a, b+l, l)
                    compression(a+l, b+l, l)
                    return
        answer[start]+=1
    
    compression(0,0,l)
    return answer
'''
l = 2 (0,0), (0,2), (2,0), (2,2)
l = 3 (0,0), (0,4), (4,0), (4,4) 이 안에서 l=2
'''