#n개로 연속된 몇 개를 선택해서 구할 수 있는 합 중 가잔 큰 합

#수를 무조건 k개 이상 선택해야 된다.


#나를 더해서 cnt +1 개를 만들거나
#나 부터 시작해서 1개로 들어가도 됨.
n, k =map(int ,input().split())
arr = [0] + [*map(int, input().split())]

prefix = [0]*(n+1)

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i]


dp = [0] * (n+1)
#k개는 연속적으로 선택했어야 하니까
dp[k] = prefix[k]
for i in range(k+1, n+1):#새로운 k개를 달성하는 것이 더 좋음
    dp[i] = max(dp[i-1] + arr[i], prefix[i] - prefix[i-k])

print(max(dp[k:]))