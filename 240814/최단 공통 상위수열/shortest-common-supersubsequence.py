s = " "+input()
t = " "+input()

dp = [[0]*(len(t)) for _ in range(len(s))]

for i in range(1,len(s)):
    for j in range(1,len(t)):
        if s[i] == t[j]:#같다면 현재 값은 
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        dp[i][j] = max(dp[i][j], dp[i][j-1],dp[i-1][j])

v = max(dp[len(s)-1])
print(len(s)+len(t)-v - 2)