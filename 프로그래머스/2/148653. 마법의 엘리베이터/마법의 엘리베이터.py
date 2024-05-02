def solution(storey):
    answer = 0
    while storey > 0:
        num = storey % 10
        
        if num > 5:
            answer += (10 - num)
            storey += (10 - num)
        elif num < 5:
            answer += num
            storey -= num
        else:
            tmp = (storey//10) % 10
            if tmp + 1 > 5:
                answer += num
                storey += num
            else:
                answer += (10 - num)
                storey -= num
        storey //= 10
    return answer