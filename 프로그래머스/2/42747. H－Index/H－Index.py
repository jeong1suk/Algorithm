def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        if n < i + 1:
            return i
    return len(citations)
    