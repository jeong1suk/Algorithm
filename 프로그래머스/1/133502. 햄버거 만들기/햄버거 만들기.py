def solution(ingredient):
    cnt = 0
    stk = []
    for i in ingredient:
        stk.append(i) # 스택에 재료 쌓기
        if stk[-4:] == [1,2,3,1]: # 순서가 맞으면 넣어주기
            cnt += 1
            
            for _ in range(4): # 순서대로 햄버거 쌓았으니까 빼주기
                stk.pop()
    return cnt
