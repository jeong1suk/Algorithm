from collections import Counter
def solution(want, number, discount):
    item_list = {i:j for i,j in zip(want, number)}
    answer = 0
    for i in range(len(discount)-9):
        dc_list = discount[i:i+10]
        if Counter(dc_list) == item_list:
            answer += 1
    return answer