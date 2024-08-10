import sys
sys.setrecursionlimit(250001)
def dfs(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]

    mx = 0
    for dx, dy in (0,1), (0,-1),(1,0),(-1,0):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >=n or ny < 0 or ny>=n:continue
        if board[nx][ny] <= board[x][y] :continue
        mx = max(mx,dfs(nx,ny))
    dp[x][y] = mx + 1
    return dp[x][y]

n = int(input())

board = [[*map(int,input().split())]for _ in range(n)]

dp = [[-1] * n for _ in range(n)]
result = -1
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i,j))
print(result)