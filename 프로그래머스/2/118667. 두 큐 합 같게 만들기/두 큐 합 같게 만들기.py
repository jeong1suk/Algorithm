from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    total = sum(queue1) + sum(queue2)
    if total%2 ==0:
        queue_total = total//2
    else:
        return -1

    count = 0
    n = len(queue1)

    # 합을 미리 구함
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 탈출 조건이 필요
    turn = 0
    while turn<3*n:

        turn+=1
        if sum2 == queue_total:
            return count

        elif sum2 > queue_total:
            tmp = queue2.popleft()
            sum2-=tmp
            queue1.append(tmp)
            sum1+=tmp
            count+=1

        elif sum2 < queue_total:
            tmp = queue1.popleft()
            sum1-=tmp
            queue2.append(tmp)
            sum2+=tmp
            count+=1

    return -1