n = int(input())
lis = [*map(int,input().split())]
lis.sort()
mid = (total:=sum(lis)) // 2#이 수를 두 번만 만들면 됨.
dp = [0]*(total+1)
dp[0] = 1
dp_num = [[]for _ in range(total+1)]
for num in lis:
    if dp[mid]:
        dp_num[mid].sort()
        for nums in dp_num[mid][::-1]:
            for i in range(mid,nums-1,-1):
                if nums in dp_num[i]:
                    dp[i] = max(dp[i]-1,0)
    for i in range(total,num-1,-1):
        dp[i] += dp[i-num]
        if dp[i]:
            dp_num[i].extend(dp_num[i-num])
            dp_num[i].append(num)
    
if dp[mid]: # 5 5 5 5 평균이 5
    print('Yes')
else:
    print('No')