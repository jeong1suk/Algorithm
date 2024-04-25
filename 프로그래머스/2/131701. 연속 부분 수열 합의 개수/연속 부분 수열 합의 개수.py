def solution(elements):
    answer = 0
    sum_arr = []
    d_elements = elements * 2
    
    sum_arr.extend(elements)
    
    n = 2
    while n <= len(elements):
        for i in range(0, len(elements)):
            new = d_elements[i:i+n]
            sum_arr.append(sum(new))
        n += 1

    answer = len(set(sum_arr))
    return answer