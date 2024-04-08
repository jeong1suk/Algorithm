def solution(name, yearning, photo):
    answer = []
    aa = dict()
    for i in range(len(name)):
        aa[name[i]] = yearning[i]
    
    for idx, names in enumerate(photo):
        # print(f"idx={idx}, names={names}")
        score = 0
        for name in names:
            for k, v in aa.items():
                if name == k:
                    score += v
        answer.append(score)
    return answer