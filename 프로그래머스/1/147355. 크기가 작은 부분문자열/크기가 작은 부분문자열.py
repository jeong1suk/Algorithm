def solution(t, p):
    answer = 0
    
    l = len(p)
    for i in range(len(t) - l):
        if t[i:i+l] <= p:
            answer += 1
    if t[-l:] <= p:
        answer += 1
    return answer