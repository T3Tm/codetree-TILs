n, m = map(int, input().split())
li = [*map(int,input().split())]

li.sort()

dp = [-1] * (m+1)
dp[0] = 0
for num in li:
    for i in range(num,m+1):
        if dp[i-num]!=-1:
            dp[i] = max(dp[i], dp[i-num]+1)
print(dp[m])