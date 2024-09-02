n = int(input())

dp = [[0] * (n+1) for _ in range(2)]


arr = [[0] + [*map(int,input().split())]for _ in range(2)]



for j in range(2):
    dp[j][1] = dp[j^1][0] + arr[j][1]

for i in range(2,n+1):
    for j in range(2):
        dp[j][i] = max(dp[j^1][i-1], dp[j^1][i-2], dp[j][i-2]) + arr[j][i]

print(max(dp[0][-1], dp[1][-1]))