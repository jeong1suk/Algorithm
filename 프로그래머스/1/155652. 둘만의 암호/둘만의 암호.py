def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in s:
        flag = 0
        idx = alphabet.index(i) # s 에 있는 단어 idx
        # print(f"idx={idx}, alphabet={alphabet[idx]}")
        
        for j in range(1, index+1):
            # j = 0,1,2,3,4
            while True:
                chk = alphabet[(idx+j+flag) % 26]
                # print(chk, flag)
                if chk not in skip:
                    break
                else:
                    flag += 1
                
            # print(f"i={i}, 스킵갯수={flag}")
        answer += alphabet[(idx+flag+index) % 26]
    return answer