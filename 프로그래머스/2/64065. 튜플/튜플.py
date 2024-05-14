def solution(s):
    answer = []
    s = s[2:-2]
    # print(s)
    s = s.split("},{")
    
    s.sort(key=lambda x:len(x))
    
    for a in s:
        li = a.split(",")
        for num in li:
            num = int(num)
            if num not in answer:
                answer.append(num)
    return answer