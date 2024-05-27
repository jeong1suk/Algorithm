def solution(record):
    answer = []
    user_id = dict()
    rec = []
    for r in record:
        op, ID = r.split()[0], r.split()[1]
        if op == 'Enter' or op == 'Change':
            name = r.split()[2]
            user_id[ID] = name

        rec.append([op, ID])
    
    for o, i in rec:
        if o == 'Enter':
            answer.append(f"{user_id[i]}님이 들어왔습니다.")
        elif o == 'Leave':
            answer.append(f"{user_id[i]}님이 나갔습니다.")

    return answer