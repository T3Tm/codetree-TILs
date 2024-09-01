def dfs(x,y):
    if x >= n or y >= n:return (1 << 63) - 1
    if x == n-1 and y == n-1:
        return arr[x][y]
    if dp[x][y]!=-1:return dp[x][y]
    dp[x][y] = max(min(dfs(x+1,y),dfs(x,y+1)),arr[x][y])
    return dp[x][y]
n = int(input())
dp = [[-1] * n for _ in range(n)]
arr = [[*map(int,input().split())]for _ in range(n)]
print(dfs(0,0))