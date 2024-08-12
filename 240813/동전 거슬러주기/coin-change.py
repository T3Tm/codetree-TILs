n , m = map(int,input().split())
li = [*map(int,input().split())]

li.sort()

dp = [10001] * (m+1)
dp[0] = 0

for num in li:
    for i in range(num,m+1):
        dp[i] = min(dp[i], dp[i-num]+1)
result = dp[m]
print([result, -1][result == 10001])