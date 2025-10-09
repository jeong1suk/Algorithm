def solution(genres, plays):
    answer = []
    dic = {}
    '''
    장르별 베스트 2개씩
    제일 많이 재생 장르 먼저 수록, 장르 내에서 많이 재생된 노래 수록, 고유 번호 낮은 노래
    classic = [500, 150, 800]
    pop = [600, 2500]
    이러면 pop 먼저고 2500 600,  classic 800 500
    장르는 100개 미만, 속한 곡이 하나일 수도 있음 play는 고유함
    '''
    for i, (genre, play) in enumerate(zip(genres, plays)):
        # print(i, genre, play)
        if genre not in dic:
            dic[genre] = {'t': 0, 'l': []}
        dic[genre]['l'].append({'v':play, 'i':i})
        dic[genre]['t'] += play
    
    dic = list(dic.values())
    # print("분류 전: ", dic)
    dic = sorted(dic, key=lambda x:x['t'], reverse=True)
    # print("sort: ", dic)
    
    for i in range(len(dic)):
        v = dic[i]['l']
        v = sorted(v, key=lambda x:x['v'], reverse=True)
        for j in range(2 if len(v) >= 2 else len(v)):
            answer.append(v[j]['i'])
    return answer