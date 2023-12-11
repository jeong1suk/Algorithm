def solution(bandage, health, attacks):
    answer = 0
    last_time = attacks[-1][0]
    # print("마지막 시간: ", last_time)
    # print("최대 체력: ", health)
    max_health = health
    idx = 0
    inarow = 0
    for i in range(0, last_time+1):
        if health <= 0: # 체력이 0보다 작다면 끝.
            return -1
        
        if i == attacks[idx][0]: # 몬스터의 공격시간
            health -= attacks[idx][1] # 체력 깎임.
            
            inarow = 0 # 연속성공 초기화
            # print(f"공격성공 체력: {health}, 시간: {i}, 공격:{attacks[idx][1]}")
            idx += 1 # 다음 공격 시간으로 넘기기.
        else:
            inarow += 1
            health += bandage[1]
            # print(f"시간:{i}, 현재 체력:{health}, 연속성공:{inarow}")
            
        if health >= max_health: # 체력이 최대체력과 같다면 연속성공 초기화
            health = max_health
            inarow = 0
        
        if inarow == bandage[0]: # t초 연속으로 붕대를 감는데 성공.
            health += bandage[2] # y 만큼 체력 추가 회복
            inarow = 0
        
        
    return health if health > 0 else -1