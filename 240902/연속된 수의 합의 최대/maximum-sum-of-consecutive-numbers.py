#n개로 연속된 몇 개를 선택해서 구할 수 있는 합 중 가잔 큰 합

#수를 무조건 k개 이상 선택해야 된다.


#나를 더해서 cnt +1 개를 만들거나
#나 부터 시작해서 1개로 들어가도 됨.

INF = 10**9
n, k =map(int ,input().split())
arr = [*map(int, input().split())]

dp = [[-INF]*(n+2) for _ in range(n+1)]#연속해서 몇 개를 선택했는지 알아야 됨.

#k개는 선택해야 하므로
#모든 곳에 k개까지는 선택하도록 만든다.

#dp[i][0] = i까지 0개 선택헀을 때
for i in range(n):
    dp[i][1] = arr[i]#1개 고르는 경우
result = -INF
for j in range(2,k+1):#1개부터 n개 고르는 경우의 수
    for i in range(n):
        if i + 1 < j:continue
        dp[i][j] = dp[i-1][j-1] + arr[i]
        if j == k:
            result = max(result, dp[i][j])

for j in range(k+1,n+1):
    for i in range(n):
        if i + 1 < j :continue
        dp[i][j] = dp[i-1][j-1] + arr[i]
        result = max(result, dp[i][j])
print(result)