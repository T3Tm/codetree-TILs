n, m = map(int,input().split())

li = [*map(int,input().split())]

li.sort()

total = max(sum(li), m)
dp = [0] * (total + 1)
dp[0] = 1

for num in li:
    for j in range(total, num-1,-1):
        dp[j] += dp[j-num]

print(["No","Yes"][dp[m]>0])