INF = 10**9 + 1
n, m = map(int, input().split())

arrn = [*map(int,input().split())] #무조건 n이 m보다 크거나 같게 만든다
arrm = [*map(int,input().split())]

if m > n:
    n,m = m,n
    tmp = arrn[::]
    arrn = arrm[::]
    arrm = tmp[::]#깊은 복사
arrn.sort(reverse=1)
arrm.sort(reverse=1)

dp = [[INF]*(n)for _ in range(m)]


def dfs(depth, index):#해당 depth에 index를 골랐을 때 최대 값
    if depth == m:
        return 0
    if index == n:return INF
    if dp[depth][index]!=INF:return dp[depth][index]

    for j in range(index, n):#depth랑 j랑 차이 계산 후 더해주기
        dp[depth][index] = min(dp[depth][index], dfs(depth+1,j+1) + abs(arrm[depth] - arrn[j]))
    return dp[depth][index]
print(dfs(0,0))