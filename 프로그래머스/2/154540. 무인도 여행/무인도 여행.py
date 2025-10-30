from collections import deque
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(maps, i, j, visited):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    area = int(maps[i][j])
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == False and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                area += int(maps[nx][ny])
                queue.append((nx, ny))
    return area

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == False:
                answer.append(bfs(maps, i, j, visited))

    return sorted(answer) if answer else [-1]