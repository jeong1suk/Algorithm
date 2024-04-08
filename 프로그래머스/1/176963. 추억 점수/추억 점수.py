def solution(name, yearning, photo):
    answer = []
    dictionary = dict(zip(name, yearning))
    
    for names in photo:
        score = 0
        for name in names:
            if name in dictionary:
                score += dictionary[name]
        answer.append(score)
    return answer