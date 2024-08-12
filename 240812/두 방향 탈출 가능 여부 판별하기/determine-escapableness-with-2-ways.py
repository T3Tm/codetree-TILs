n,m=map(int,input().split())

board = [[*map(int,input().split())] for _ in range(n)]

visited=[[0]*m for _ in range(n)]
visited[0][0] = 1

s = [(0,0)]
while s:
    x,y = s.pop()
    for dx,dy in (0,1),(1,0):
        nx,ny = x + dx, y +dy
        if nx < 0 or nx >=n or ny < 0 or ny >=m:continue
        if visited[nx][ny] or not board[nx][ny]:continue
        visited[nx][ny] = 1
        s.append((nx,ny))

print(visited[n-1][m-1])