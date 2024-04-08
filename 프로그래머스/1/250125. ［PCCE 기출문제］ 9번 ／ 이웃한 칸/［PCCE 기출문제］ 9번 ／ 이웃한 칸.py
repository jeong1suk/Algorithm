def solution(board, h, w):
    answer = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    color = board[h][w]
    n = len(board)


    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if h_check < 0 or w_check < 0:
            continue
        if h_check >= n or w_check >= n:
            continue
        if color == board[h_check][w_check]:
            answer += 1

    return answer