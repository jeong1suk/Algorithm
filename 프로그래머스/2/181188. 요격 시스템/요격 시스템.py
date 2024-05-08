def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    x = 0
    for target in targets:
        if x <= target[0]:
            x = target[1]
            answer+=1
    return answer