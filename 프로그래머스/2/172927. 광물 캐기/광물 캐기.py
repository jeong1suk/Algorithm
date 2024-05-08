def solution(picks, minerals):
    answer = 0
    dict = {'diamond':25, 'iron':5, 'stone':1}
    inven = list()
    for i in range(sum(picks)):
        count = 0
        s = minerals[i*5: i*5+5]
        if len(s) > 0:
            for j in s:
                count += dict[j]
            inven.append([s, count, i])
    inven.sort(key=lambda x:x[1])
    # print(inven)
    
    while inven:
        if picks[0] != 0:
            answer += len(inven[-1][0])
            picks[0] -= 1
        elif picks[1] != 0:
            for mineral in inven[-1][0]:
                if mineral == 'diamond':
                    answer += 5
                else:
                    answer += 1
            picks[1] -= 1
        else:
            for mineral in inven[-1][0]:
                if mineral == 'diamond':
                    answer += 25
                elif mineral == 'iron':
                    answer += 5
                else:
                    answer += 1
            picks[2] -= 1
        inven.pop()
    return answer