def solution(data, ext, val_ext, sort_by):
    # 코드번호, 제조일, 최대수량, 현재수량

    answer = []
    values = ['code', 'date', 'maximum', 'remain']
    index = values.index(ext)
    sort_idx = values.index(sort_by)
    
    for idx, da in enumerate(data):
        if da[index] <= val_ext:
            answer.append(da)
            # if not answer:
            #     min_val = da[sort_idx]
            #     answer.append(da)
            # else:
            #     if min_val > da[sort_idx]:
            #         tmp = answer.pop(0)
            #         answer.append(da)
            #         answer.append(tmp)
            #         min_val = da[sort_idx]
    return sorted(answer, key=lambda a:(a[sort_idx]))