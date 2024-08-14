def d(x,y,t):
    if x == n+1:
        return 0
    if dp[x][y][t] !=-1 :return dp[x][y][t]
    for i in range(1,m+1):
        if i == t:continue
        dp[x][y][t] = max(dp[x][y][t], d(x+1,i,i)+board[x][i])
    return dp[x][y][t]
n,m = map(int,input().split())
dp = [[[-1]*(m+1) for _ in range(m+1)] for _ in range(n+1)]
board =[[0] * 4 ] + [[0] + [*map(int,input().split())] for _ in range(n)]
print(d(0,0,0))