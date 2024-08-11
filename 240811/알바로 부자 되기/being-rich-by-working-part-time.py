from bisect import bisect_left
n = int(input())
dp = [0]
end_line = [0]
    
for i in range(n):
    s,e,p = map(int,input().split())
    
    now = 0
    for j in range(i):
        if end_line[j] < s:
            now = max(now,dp[j])
    dp.append(now + p)
    end_line.append(e)
print(max(dp))