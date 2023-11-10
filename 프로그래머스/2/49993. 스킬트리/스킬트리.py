from collections import defaultdict
def solution(skill, skill_trees):
    result = 0
    sp = defaultdict(int)
    for i, s in enumerate(skill):
        sp[s] += i + 1 # 없는 값은 0으로 처리하기 때문
    # print(sp)
    # 숫자가 작은게 먼저 나와야 한다.
    # 스킬트리는 무조건 1->2->3->... 순으로 진행돼야한다.
    for k in skill_trees:
        flag = 1 # 먼저 나온 스킬트리의 번호를 저장하는 변수
        for i in range(0, len(k)):
            # print(sp[k[i]], end=" ")
            if sp[k[i]] == 0: # 스킬트리가 없는건 무시
                continue
            elif sp[k[i]] == flag: # 스킬트리 순서에 맞는 것
                flag += 1
            else: # 순서 안 맞으면 빠져나가기
                flag = -1
                break
        # print()
        if flag != -1:
            result += 1
    return result