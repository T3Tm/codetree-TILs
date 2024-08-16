import sys
sys.setrecursionlimit(10001)
n = int(input())

board = [[*map(int,input().split())]for _ in range(n)]

visited = [[-1] * n for _ in range(n)]
def dfs(x, y, gap, mini, vis):
    visited[x][y] = vis
    if x == n-1 and y == n-1:
        return 1
    
    for dx, dy in (0,1), (0,-1),(1,0), (-1,0):
        nx ,ny = x + dx, y + dy
        if nx < 0 or nx >=n or ny < 0 or ny >=n:continue
        if visited[nx][ny] == vis:continue
        if board[nx][ny] < mini or board[nx][ny] > mini + gap:continue
        ret = dfs(nx, ny, gap, mini, vis)

        if ret:return 1
    return 0
flag = 0

v = 0
for gap in range(1, 101):
    for mini in range(1, 101):
        if board[0][0] < mini or board[0][0] > mini + gap:continue
        if dfs(0,0, gap, mini, v):
            print(gap)
            flag = 1
            break
        v+=1
    if flag:break