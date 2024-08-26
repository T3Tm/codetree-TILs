import sys
sys.setrecursionlimit(2002)
input = sys.stdin.readline

def dfs(x,y):
    global n
    if x > y:return 0
    if dp[x][y]!=-1:return dp[x][y]
    day = (n-y-1) + x + 1
    dp[x][y] = max(dfs(x+1,y) + arr[x]*day, dfs(x,y-1)+arr[y]*day)
    return dp[x][y]
n = int(input())

arr = [int(input())for _ in range(n)]

dp = [[-1]*n for _ in range(n)]

print(dfs(0,n-1))