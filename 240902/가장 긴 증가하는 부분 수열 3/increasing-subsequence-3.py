a = int(input())


dp =[0] * 1001

for i in map(int ,input().split()):
    dp[i] = max(dp[i], max(dp[:i])+1)
print(max(dp))