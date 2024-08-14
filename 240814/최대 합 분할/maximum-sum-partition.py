n = int(input())
# total이 있다면 

li = [0] + [*map(int,input().split())]
total = sum(li)
dp = [[-1] * (total + 1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0

for i in range(1,n+1):
    for j in range(total+1):
        if j + li[i] <= total and dp[i-1][j+li[i]]!=-1:
            dp[i][j] = dp[i-1][j + li[i]]
        
        #차이가 j를 만들 수 있다면 나를 더 넣어서 차이를 줄일 수 있다.
        if j - li[i] >= 0 and dp[i-1][j - li[i]]!= -1 :
            dp[i][j] = max(dp[i][j], dp[i-1][j - li[i]] + li[i])
        
        if dp[i-1][abs(j-li[i])]!=-1: 
            dp[i][j] = max(dp[i][j], dp[i-1][abs(j-li[i])] - abs(j-li[i]) + li[i])
        #자기 자신은 그대로 빠짐
        dp[i][j] = max(dp[i-1][j],dp[i][j])
result = 0
for i in range(1,n+1):
    result = max(result, dp[i][0])
print(result)