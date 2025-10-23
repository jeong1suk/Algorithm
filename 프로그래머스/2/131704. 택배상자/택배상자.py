def solution(order):
    box = [] # 예비 컨테이너
    N = len(order)
    i = 1
    idx = 0
    
    while i < N + 1:
        box.append(i)
        while box[-1] == order[idx]:
            idx += 1
            box.pop()
            if len(box) == 0:
                break
        i += 1
            
    return idx