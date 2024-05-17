'''
if 원판이 2개 이상
    덩어리 이동 from 시작기둥 to 보조기둥
    이동 from 시작기둥 to 대상기둥
    덩어리 이동 from 보조기둥 to 대상기둥
'''
def solution(n):
    def hanoi(floor, start, target, temp):
        if floor == 1:
            return [[start, target]]
        # 제일 아래 원판 제외하고 덩어리를 보조기둥으로 옮김
        # 제일 아래 원판을 target으로 옮김.
        return hanoi(floor-1, start, temp, target) + [[start, target]] + hanoi(floor-1, temp, target, start)
    return hanoi(n, 1, 3, 2)