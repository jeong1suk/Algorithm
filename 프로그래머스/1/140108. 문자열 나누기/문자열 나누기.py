def solution(s):
    string = []
    while s:
        first = s[0]
        left = s[1:]
        # print(f"첫번째 문자={first}, 나머지문자열={left}")
        same, diff = 1, 0
        for i in range(len(left)):
            if first == left[i]: # 문자가 같다면
                same += 1
            else: # 문자가 다르면
                diff += 1
            if same == diff:
                break
        string.append(s[:same+diff])
        s = s[same+diff:]
        # print(f"string={string}, 자른 s= {s}")

    
    return len(string)