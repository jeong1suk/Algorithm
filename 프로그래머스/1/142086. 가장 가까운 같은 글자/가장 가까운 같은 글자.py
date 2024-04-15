def solution(s):
    answer = []
    alpha = dict()
    for i, c in enumerate(s):
        if c in alpha.keys():
            q = alpha[c]
            answer.append(i-q)
        else:
            answer.append(-1)
        alpha[c] = i

    return answer