def solution(n, stations, w):
    answer = 0
    start = 1
    cover = 2*w + 1
    for s in stations:
        left, right = s - w, s + w
        if start < left:
            length = left - start
            answer += (length + cover - 1) // cover
        start = right + 1
        
    if start <= n:
        length = n - start + 1
        answer += (length + cover - 1) // cover
    return answer