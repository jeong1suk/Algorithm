def tri_sum(tri, point, memo):
    if point[0] + 1 > len(tri): # 제일 마지막 층이라면 되돌아가기
        return 0
    if memo[point[0]][point[1]] != -1: # 값이 -1이 아니라면 최대합을 구한거라서 중복을 피함 
        return memo[point[0]][point[1]]
    left_sum = tri[point[0]][point[1]] + tri_sum(tri, [point[0] + 1, point[1]], memo)
    right_sum = tri[point[0]][point[1]] + tri_sum(tri, [point[0] + 1, point[1] + 1], memo)
    # 왼쪽 합, 오른쪽 합을 구하고, 최대값을 저장
    memo[point[0]][point[1]] = max(left_sum, right_sum)
    return memo[point[0]][point[1]]

def solution(triangle):
    memo = [[-1] * len(row) for row in triangle]
    # 각 위치에서의 최대 합을 저장하고 최대합이 있으면 중복계산을 피함
    return tri_sum(triangle, [0, 0], memo)