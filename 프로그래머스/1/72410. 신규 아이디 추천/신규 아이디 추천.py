def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계
    # 2단계
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
            
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
            
    # 4단계
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    
    if answer[-1] == '.':
        answer = answer[:len(answer)-1]
    # 5단계
    if answer == '':
        answer += 'a'
    
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:14]
    
    # 7단계
    if len(answer) <= 2:
        last = answer[-1]
        while len(answer) <= 2:
            answer += last
            
    return answer