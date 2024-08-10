n = int(input())

board = [[0]*(n+1)] + [[0] + [*map(int,input().split())]for _ in range(n)]

dp = [[-1] * (n+1) for _ in range(n+1)]


data = [(board[i][j],i,j) for i in range(1,n+1) for j in range(1,n+1)]

data.sort(key = lambda x: (x[0]))

result = -1
for value, x, y in data:
    dp[x][y] = max(dp[x][y], 1)
    
    for dx, dy in (0,1), (0,-1),(1,0),(-1,0):
        nx, ny = x + dx, y +dy
        
        if nx < 1 or nx > n or ny < 1 or ny> n:continue
        if board[nx][ny] <= value:continue
        dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)
        result = max(result, dp[nx][ny])
print(result)