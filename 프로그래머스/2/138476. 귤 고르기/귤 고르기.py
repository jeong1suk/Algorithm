def solution(k, tangerine):
    answer = 0
    cnt = dict()
    for t in tangerine:
        if t in cnt.keys():
            cnt[t] += 1
        else:
            cnt[t] = 1
    # print(cnt)
    sor = sorted(cnt.values(), reverse=True)
    for s in sor:
        k -= s
        answer += 1
        if k <= 0:
            break
    return answer