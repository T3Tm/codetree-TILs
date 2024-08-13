n = int(input())
li = [0] + [*map(int,input().split())]

dp = [0] * (n+1)
#dp[i] = i원일 때 최대 수익 저장
for i in range(1,n+1):#i원일 때
    for num in range(1,n+1):#num의 숫자들로
        if num > i:break
        dp[i] = max(dp[i],dp[i-num] + li[num])
print(dp[n])