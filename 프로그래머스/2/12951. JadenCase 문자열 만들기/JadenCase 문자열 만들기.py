def solution(s):
    answer = []
    print(s.split(' '))
    for word in s.split(' '):
        if word != "":
            answer.append(word.capitalize())
        else:
            answer.append("")
        
    return ' '.join(answer)

'''
def solution(s):
    answer = ''
    s = s.split()
    print(s)
    for i in s:
        answer += i.capitalize() + ' '

    return answer.rstrip()
'''