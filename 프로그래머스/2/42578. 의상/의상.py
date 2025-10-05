def solution(clothes):
    answer = 1
    closet = {}
    for name, cate in clothes:
        if cate in closet.keys():
            closet[cate] += [name]
        else:
            closet[cate] = [name]
    
    for _, value in closet.items():
        answer *= (len(value) + 1)
    
    return answer - 1