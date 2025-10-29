from collections import Counter
def solution(topping):
    answer = 0
    # 토핑이 더 중요
    # prefix, suffix 집합 크기를 미리 구해놓고 한 번의 순회로 해결할 수 있습니다.
    # 왼쪽에서부터 토핑 종류 개수를 누적
    # 오른쪽에서부터 토핑 종류 개수를 누적
    # 두 배열을 비교
    right = Counter(topping)
    left = set()
    print(right, len(right))
    
    for t in topping:
        left.add(t)
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        
        if len(left) == len(right):
            answer += 1
            
    return answer