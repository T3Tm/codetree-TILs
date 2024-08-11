n = int(input())
lis = [*map(int,input().split())]
lis.sort()
mid = sum(lis) // 2#이 수를 두 번만 만들면 됨.
dp = [[0]*(10**5+1) for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1
ptr = 0
for num in lis:
    for i in range(10**5,num-1,-1):
        dp[ptr][i] += dp[ptr][i-num]
    if dp[ptr][mid]:
        ptr += 1
if ptr==2:
    print('Yes')
else:
    print('No')