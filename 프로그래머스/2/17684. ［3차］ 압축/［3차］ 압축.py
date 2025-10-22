def solution(msg):
    answer = []
    # a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # dic = {j: i+1 for i, j in enumerate(a)}
    dic = {chr(65+i): i+1 for i in range(26)}
    dict_idx = 27
    i = 0
    while i < len(msg):
        w = msg[i] # 2번
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 찾기
        while i + len(w) < len(msg) and msg[i:i+len(w)+1] in dic:
            w = msg[i:i+len(w)+1]
        # 3번
        answer.append(dic[w])
        i += len(w)
        # 4번 사전 초기화
        if i < len(msg):
            dic[w + msg[i]] = dict_idx
            dict_idx += 1
            
    return answer