#n개로 연속된 몇 개를 선택해서 구할 수 있는 합 중 가잔 큰 합

#수를 무조건 k개 이상 선택해야 된다.


#나를 더해서 cnt +1 개를 만들거나
#나 부터 시작해서 1개로 들어가도 됨.

INF = 10**9
n, k =map(int ,input().split())
arr = [*map(int, input().split())]

prefix = [0]*(n+1)

for i in range(1, k+1):
    prefix[i] = prefix[i-1] + arr[i-1]

#k개는 연속적으로 선택했어야 하니까

for i in range(k+1, n+1):
    prefix[i] = max(prefix[i-1] + arr[i-1], prefix[i-1] + arr[i-1] - prefix[i-k])

print(max(prefix[k:]))