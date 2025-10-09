def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)] # 방문 여부 체크하는 배열
    
    for com in range(n):
        if visited[com] == False: # 방문하지 않은 노드들만 확인
            DFS(n, computers, com, visited) # DFS
            answer += 1 # 네트워크 확인하고 난 뒤에는 +1
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True # 방문했으니까 True로 바꿔주고
    
    for i in range(n):
        # 확인하는 거랑 다른 인덱스, 네트워크 연결, 방문x
        if i != com and computers[i][com] == 1 and visited[i] == False:
            DFS(n, computers, i, visited)