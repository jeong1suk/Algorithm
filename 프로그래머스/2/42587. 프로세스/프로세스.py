'''
우선 순위마다 위치(=순서)을 갖는 목록 만들기
만든 목록에서 왼쪽 부터 추출하기
만약 추출 된 우선 순위가 남은 목록의 우선 순위들 중 작은 경우가 존재 시, 다시 목록의 오른쪽으로 추가하기
존재 하지 않을 시, 처리 횟수 증가한다. 만약 위치(=순서)가 동일한 경우는 반환하기
'''
from collections import deque
def solution(priorities, location):
    answer = 0
    data = deque(enumerate(priorities))
    while data:
        idx, p = data.popleft()
        if not data:
            return answer+1
        max_idx, max_p = max(data, key=lambda x:x[1])
        if p < max_p:
            data.append((idx, p))
        else:
            answer += 1
            if idx == location:
                return answer