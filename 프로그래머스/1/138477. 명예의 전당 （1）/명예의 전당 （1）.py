def solution(k, score):
    answer = []
    top_k = []

    for i in range(len(score)):
        top_k.append(score[i])
        top_k.sort(reverse=True)
        if len(top_k) > k:
            del top_k[-1]
        answer.append(top_k[-1])

    return answer