def solution(friends, gifts):
    answer = 0
    present_idx = {name: index for index, name in enumerate(friends)}
    present = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    gift_idx = [] # 선물 지수
    for gift in gifts:
        give, take = gift.split(" ")
        g_idx, t_idx = present_idx[give], present_idx[take]
        # print(f"준 사람={give} idx={present_idx[give]}, 받은 사람={take} idx={present_idx[take]}")
        present[g_idx][t_idx] += 1
    # print(present)
    # print([row[0] for row in present])
    # print(sum([row[0] for row in present]))
    for i in range(len(friends)):
        row_sum = sum(present[i])
        col_sum = sum(row[i] for row in present)
        gift_idx.append(row_sum - col_sum)
    # print(gift_idx)
    
    for i in range(len(friends)):
        tmp_g = 0
        for j in range(len(friends)):
            if i == j:
                continue
            if present[i][j] > present[j][i]:
                tmp_g += 1
            elif present[i][j] == present[j][i]:
                tmp_g = tmp_g+1 if gift_idx[i] > gift_idx[j] else tmp_g
                
        answer = max(answer, tmp_g)

    return answer