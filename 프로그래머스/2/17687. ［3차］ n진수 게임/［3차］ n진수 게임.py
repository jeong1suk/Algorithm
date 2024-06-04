def solution(n, t, m, p):
    answer = '0'
    notation = '0123456789ABCDEF'
    
    for num in range(m*t):
        result = ""
        while num > 0:
            num, mod = divmod(num, n)
            result += notation[mod]
        answer += result[::-1]

    return answer[p-1::m][:t]
'''
0 1 1 0 1 1 100 101 110 111
0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 13 14 15 16 17 18 19 1A 1B
'''