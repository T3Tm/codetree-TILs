n, m = map(int, input().split())

arrn = [*map(int,input().split())] 
arrm = [*map(int,input().split())]

n = len(arrn)
m = len(arrm)
if m > n:#무조건 n이 m보다 크거나 같게 만든다
    n,m = m,n
    tmp = arrn[::]
    arrn = arrm[::]
    arrm = tmp[::]#깊은 복사
arrn.sort() #역순으로 정렬한다.
arrm.sort()

dp = [[-1]*(n)for _ in range(m)]
#여기서 해야 되는 것이 m이 무조건 작음
#n - m 
def dfs(depth, index):#해당 depth에 index를 골랐을 때 최대 값
    if depth == m:
        return 0
    if index >= n:return 10**9 + 1
    if dp[depth][index]!=-1:return dp[depth][index]

    for j in range(index, n-(m-depth)+1):#depth랑 j랑 차이 계산 후 더해주기 n - (m - (depth+1))
        ret = dfs(depth+1,j+1) + abs(arrm[depth] - arrn[j])
        if dp[depth][index] == -1:dp[depth][index] = ret
        else : dp[depth][index] = min(dp[depth][index],ret)
    return dp[depth][index]
print(dfs(0,0))