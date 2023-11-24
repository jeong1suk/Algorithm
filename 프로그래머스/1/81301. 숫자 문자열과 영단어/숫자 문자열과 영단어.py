def solution(s):
    answer = ''
    digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # print(digit.get('nin'))
    
    eng = ''
    # print(eng, type(eng), digit.get(eng))
    
    for c in s:
        if c.isdigit():
            answer += str(c)
        else:
            eng += c
        
        if digit.get(eng):
            answer += digit[eng]
            eng = ''
    
    return int(answer)