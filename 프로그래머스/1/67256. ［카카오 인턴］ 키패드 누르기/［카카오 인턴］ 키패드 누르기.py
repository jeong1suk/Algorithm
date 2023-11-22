def solution(numbers, hand):
    answer = ''
    keyboard = [[1,2,3], [4,5,6], [7,8,9], ['*',11,'#']]
    L, R = 10, 12
    for num in numbers:
        if num == 0:
            num = 11
        if num in [1,4,7]:
            answer += 'L'
            L = num
        elif num in [3,6,9]:
            answer += 'R'
            R = num
            
        else: # 2 5 8 0 거리 계산 하기
            l_left = abs(L - num) % 3 + abs(L - num) // 3
            r_left = abs(R - num) % 3 + abs(R - num) // 3
            # print(f"왼손 위치={L}, 오른손위치={R}, 눌러야할번호={num}, 차이={l_left}, {r_left}")
            # print(l_left, r_left)
            if l_left < r_left:
                answer += 'L'
                L = num
            elif r_left < l_left:
                answer += 'R'
                R = num
            else: # 거리가 같을 때
                if hand == 'right':
                    answer += 'R'
                    R = num
                else:
                    answer += 'L'
                    L = num

    return answer