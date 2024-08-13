n, m = map(int,input().split())

li = [[*map(int,input().split())]for _ in range(n)]
li.sort()



dp = [-1]*(m+1)
dp[0] = 0
for (w,v) in li:
    for i in range(m,w-1,-1):
        if dp[i-w]!= -1:
            dp[i] = max(dp[i],dp[i-w] + v)
print(max(dp))