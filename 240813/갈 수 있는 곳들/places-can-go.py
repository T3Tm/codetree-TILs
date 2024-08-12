from collections import deque
n,k = map(int,input().split())

board = [[*map(int,input().split())]for _ in range(n)]

q = deque()
visited= [[0]*n for _ in range(n)]
for _ in range(k):
    x,y = map(int,input().split())
    visited[x-1][y-1] = 1
    q.append((x-1,y-1))

cnt = 0
while q:
    x,y = q.popleft()
    cnt += 1
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        nx,ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >=n:continue
        if board[nx][ny] or visited[nx][ny]:continue
        visited[nx][ny] = 1
        q.append((nx,ny))
print(cnt)