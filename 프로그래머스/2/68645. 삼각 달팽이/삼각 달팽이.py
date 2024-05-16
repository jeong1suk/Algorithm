def solution(n):
    answer = []
    tri = [[0 for _ in range(n)] for _ in range(n)] # 이차원 배열에 저장하기.
    num = 1
    x, y = 0, 0
    dir = 0
    while num <= n*(n+1) // 2:
        tri[x][y] = num
        # 아래로 내려가기 tri[D][R] D += 1
        # 오른쪽 tri[D][R] R += 1
        # 위 tri[U][n-R] U -= 1
        
        if dir == 0 and (x == n-1 or (x < n-1 and tri[x+1][y] != 0 )):
            dir = 1 # 오른쪽
        elif dir == 1 and (y == n-1 or (y < n-1 and tri[x][y+1] != 0)):
            dir = 2 # 위
        elif dir == 2 and (x > 0 and tri[x-1][y-1] != 0):
            dir = 0 # 아래
            
        if dir == 0:
            x += 1
        elif dir == 1:
            y += 1
        elif dir == 2:
            x -= 1
            y -= 1
            
        if num == n*(n+1)//2:
            break

        num += 1
    index = 0
    for i in range(0, n):
        for j in range(0, n):
            if tri[i][j] != 0:
                answer.append(tri[i][j])
                index += 1
    return answer