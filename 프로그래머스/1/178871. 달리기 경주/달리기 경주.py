def solution(players, callings):
    p_dict = {player: idx for idx, player in enumerate(players)}
    # print(p_dict)
    for name in callings:
        # print(player_dict[name])
        idx = p_dict[name]
        
        name1, name2 = players[idx-1], players[idx]
        # print(f"calling={name}, 앞={name1}, 뒤={name2}")
        p_dict[name1] += 1
        p_dict[name2] -= 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
    # print(players)
    return players