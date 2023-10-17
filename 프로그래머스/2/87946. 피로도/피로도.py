from itertools import permutations
def solution(k, dungeons):
    # 최소 필요 피로도,
    # 소모 피로도
    # 던전을 최대한 많이 탐험.
    # k = 유저의 현재 피로도, 1 < k < 5000
    # [최소 필요 피로도, 소모 피로도] 던전은 최대 8개
    # 최대 던전 수 return하기
    answer = -1
    # 던전이 최대 8개 이므로 최악의 경우의 수는 8! = 40320,
    # 순열로 모든 경우의 수 계산하기.
    for p in permutations(dungeons, len(dungeons)):
        # print(p)
        temp_k = k
        cnt = 0
        
        for mini, use in p:
            #mini = 최소 필요 피로도, use = 소모 피로도
            if temp_k >= mini:
                temp_k -= use
                cnt += 1
        
        answer = max(answer, cnt)
        # 던전의 길이랑 같으면 바로 return
        if answer == len(dungeons):
            return answer
    return answer