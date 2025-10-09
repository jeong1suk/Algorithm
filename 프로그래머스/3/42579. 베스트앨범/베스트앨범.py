def solution(genres, plays):
    answer = []
    d1 = {}
    d2 = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in d1:
            d1[genre] = [(i, play)]
        else:
            d1[genre].append((i, play))
        
        if genre not in d2:
            d2[genre] = play
        else:
            d2[genre] += play
    # print(d1)
    # print(d2)
    for (k, v) in sorted(d2.items(), key=lambda x:x[1], reverse=True):
        # print(k, v)
        for (i, p) in sorted(d1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer