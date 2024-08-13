n = int(input())
li = [*map(int,input().split())]
li.sort()
mid = (total:=sum(li)) // 2#이 수를 두 번만 만들면 됨.

dp = [0]*(total+1)
dp[0] = 1

#합이 n이 되는 순간이 있는 지 확인
#그럼 다른 순간은 무조건 n이 됨.

result = 10 ** 8
for i in range(n):
    for j in range(total,li[i]-1,-1):
        if dp[j-li[i]]:
            dp[j] = 1
        
        if j == mid and dp[j]:
            result = mid

if total - (result*2) == 0:
    print('Yes')
else:
    print('No')