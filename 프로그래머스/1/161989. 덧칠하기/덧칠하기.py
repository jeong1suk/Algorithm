def painting(walls,start,end):
    for n in range(start, end):
        walls[n] = True
    return walls
def solution(n, m, section):
    answer = 0
    walls = [True] * n
    
    for paint in section:
        walls[paint-1] = False
    
    for i in range(n-m+1):
        if walls[i] == False:
            painting(walls, i, i+m)
            answer += 1

    if sum(walls) != n:
        return answer + 1
    return answer