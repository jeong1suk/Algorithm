def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # badguy = []
    id_dict = {name: [] for name in id_list} # 신고한 사람 넣는 dict
    report_cnt = {name: 0 for name in id_list} # 신고당한 횟수 체크
    # print(id_dict)
    for name_list in report:
        sender, bad = name_list.split(' ')
        # print(sender, bad)
        
        if sender not in id_dict[bad]:
            id_dict[bad].append(sender)
    # print(id_dict)
    # print("신고당한 횟수: ", report_cnt)
    for key, value in id_dict.items():
        if len(value) >= k:
            # print(key)
            for name in value:
                report_cnt[name] += 1
    # print(report_cnt)
    '''         
    for key, value in report_cnt.items():
        # print(f"key = {key}, {value}, ", type(value))
        if value >= k:
            print(f" 신고당한사람 = {key}, 신고횟수:{value}")
            # badguy.append(key)
    
    # for bad in badguy:
        # if bad in 
    '''
    return [cnt for cnt in report_cnt.values()]