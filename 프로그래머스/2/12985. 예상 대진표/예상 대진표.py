def solution(n,a,b):
    answer = 1
    a, b = max(a,b), min(a,b) # b가 항상 크게 세팅
    
    while True:
        if (b+1) // 2 == (a+1) // 2:
            return answer
        else:
            a = (a + 1) // 2
            b = (b + 1) // 2
            answer += 1

'''
  4      7
 24     57
12 34 56 78 
첫번째 라운드 4 7 
두번째 2 4
세번째 1 2
4 2(=4/2) 1(=2/2)
7 4(=7+1 / 2) 2=(4/2)
a든 b든 +1 한 다음에 // 2 한 게 다음 라운드 값.
'''