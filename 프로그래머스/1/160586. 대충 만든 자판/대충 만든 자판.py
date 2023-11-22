def solution(keymap, targets):
    answer = []
    # keymap 돌면서 dict에 알파벳 할당 key에 알파벳, value에 눌러야하는 키보드 갯수
    keyboard = {}
    # print(keyboard.get('A')) # 없으면 None
    for board in keymap:
        for i in range(len(board)):
            if keyboard.get(board[i]) is None:
                keyboard[board[i]] = i + 1
            else:
                if keyboard[board[i]] > i:
                    keyboard[board[i]] = i + 1
    
    for target in targets:
        sum = 0
        for c in target:
            if keyboard.get(c) is None:
                sum = -1
                break
            else:
                sum += keyboard[c]
        answer.append(sum)
    return answer