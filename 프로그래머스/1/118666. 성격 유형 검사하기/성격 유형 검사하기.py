def find_character(character, c1, c2):
    # print(character[c1], type(character[c1]))
    if character[c1] < character[c2]:
        return c2
    
    return c1

def solution(survey, choices):
    answer = ''
    character = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }
    # 점수는 4점을 기준으로 바뀐다.
    # 점수가 음수면 첫번째, 양수면 두번째
    for char, score in zip(survey, choices):
        if score < 4:
            character[char[0]] +=  4 - score
        elif score > 4:
            character[char[1]] += score - 4
    # find_character(character, 'R', 'T')
    answer += find_character(character, 'R', 'T')
    answer += find_character(character, 'C', 'F')
    answer += find_character(character, 'J', 'M')
    answer += find_character(character, 'A', 'N')
    return answer