from collections import deque

n,m = map(int,input().split())

board =[[*map(int,input().split())]for _ in range(n)]

visited=[[0]* m for _ in range(n)]

visited[0][0] = 1
q = deque([[0,0]])
while q:
    x,y = q.popleft()
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        nx,ny = x + dx, y+dy
        if nx < 0 or nx >=n or ny < 0 or ny >=m:continue
        if not board[nx][ny] or visited[nx][ny]:continue
        visited[nx][ny] = 1
        q.append((nx,ny))
print(visited[n-1][m-1])