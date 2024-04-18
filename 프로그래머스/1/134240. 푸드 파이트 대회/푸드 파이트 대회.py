def solution(food):
    answer = ''

    for i, f in enumerate(food[1:]):
        if f % 2 != 0:
            f -= 1
        cnt = f // 2
        answer = answer + str(i+1) * cnt
        
    return answer + '0' + answer[::-1]