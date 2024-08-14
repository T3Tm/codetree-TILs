n,m = map(int,input().split())

dp = [[0]*(10001) for _ in range(n+1)]

quest = [[0,0]] + [[*map(int,input().split())]for _ in range(n)]

for i in range(1, n+1):
    e,t = quest[i]
    for j in range(1,10001):
        #골랐다면 t시간 만큼 흘렀다는 것임
        if t <= j:
            dp[i][j] = max(dp[i][j],dp[i-1][j-t] + e)
        #이번 퀘스트는 고르지 않고 그냥 넘어갔을 시
        dp[i][j] = max(dp[i][j],dp[i-1][j])


result = -1
for i in range(1,10001):
    if dp[n][i] >= m:
        result = i
        break
print(result)