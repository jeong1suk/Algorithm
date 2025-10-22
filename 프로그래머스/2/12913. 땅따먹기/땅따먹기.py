def solution(land):
    n = len(land)
    dp = [land[0][:]]
    
    for i in range(1, n):
        dp.append([0] * 4)
        for j in range(0, 4):
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if j != k)
    
    return max(dp[n-1])