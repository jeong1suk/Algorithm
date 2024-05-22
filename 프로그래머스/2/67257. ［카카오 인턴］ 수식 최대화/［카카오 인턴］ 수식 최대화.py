import re
from itertools import permutations

def solution(expression):
    operators = [i for i in expression if not i.isdigit()]
    numbers = re.split('[\+\-\*]', expression)
    per = permutations(list(set(operators)))
    answer = []
    # print(f"operators={operators}, numbers={numbers}, per={list(per)}")
    for per_list in per:
        operator = operators[:]
        number = numbers[:]
        for op in per_list:
            idx = 0
            while idx < len(operator):
                k = operator[idx]
                if op == k:
                    operator.pop(idx)
                    if k == '+':
                        number[idx] = str(int(number[idx]) + int(number.pop(idx+1)))
                    elif k == '-':
                        number[idx] = str(int(number[idx]) - int(number.pop(idx+1)))
                    else:
                        number[idx] = str(int(number[idx]) * int(number.pop(idx+1)))
                else:
                    idx += 1
        answer.append(abs(int(number[0])))
        
    return max(answer)