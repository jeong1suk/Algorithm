def solution(t, p):
    answer = 0
    
    l = len(p)
    for i in range(len(t) - len(p) + 1):
        if t[i:i+len(p)] <= p:
            answer += 1
    return answer