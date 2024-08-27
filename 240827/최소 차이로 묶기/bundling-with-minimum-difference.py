import sys
sys.setrecursionlimit(2020)
INF = 10**9 + 1
def dfs(x, y):
    global maxi
    if y == m:return 0
    if x == n:return INF
    if dp[x][y]!=INF:return dp[x][y]
    dp[x][y] = min(dfs(x+1, y), dfs(x+1,y+1) + abs(N[x]-M[y]))
    return dp[x][y]

n, m = map(int, input().split())

N = [0] + [*map(int, input().split())]
M = [0] + [*map(int, input().split())]
assert m == (len(M) -1)

if m > n:
    n,m = m,n
    tmp = N[::]
    N = M[::]
    M = tmp[::]
N.sort()
M.sort()
n,m = n+1,m+1
dp = [[INF] * m for _ in range(n)]
print(dfs(1,1))