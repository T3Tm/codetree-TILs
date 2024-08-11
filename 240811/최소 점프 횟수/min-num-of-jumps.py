def dfs(cur):
    global n, dp,li
    if cur >= n:
        if cur == n:
            return 0
        return 11
    if dp[cur] !=12: return dp[cur]
    for i in range(1,li[cur]+1):
        dp[cur] = min(dp[cur], dfs(cur + i)+1)
    return dp[cur]    
dp = [12] * 12
n = int(input())
li = [0] + [*map(int,input().split())]
v = dfs(1)
print([v ,-1][v == 12])