from collections import defaultdict
def solution(n, w, num):
    answer = 0
    # 인덱스 짝수(홀수줄)은 왼쪽에서부터, 인덱스 홀수(짝수줄)은 오른쪽에서부터
    # start_number = w * i + 1 # i = 0,1,...
    lane = n // w + 1
    num_list = [[0 for _ in range(w)] for _ in range(lane)]
    
    for i in range(lane):
        if i % 2 == 0: # 홀수 줄, 왼쪽에서부터 시작
            start_num = w * i + 1
            flag = 1
        else: # 짤수 줄, 오른쪽에서부터 시작
            start_num = w * (i + 1)
            flag = -1
        for j in range(w):
            now = start_num + j * flag
            if now > n:
                continue
            if now == num:
                answer = lane - i
                index = j
            # print(now, end=" ")
            num_list[i][j] = now
        # print()
    # print(num_list)
    return answer if num_list[-1][index] != 0 else answer - 1