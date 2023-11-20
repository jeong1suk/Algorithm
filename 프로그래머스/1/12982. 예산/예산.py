def solution(d, budget):
    
    if sum(d) <= budget:
        return len(d)
    
    d.sort()
    for idx, cost in enumerate(d):
        budget -= cost

        if budget < 0 :
            return idx
