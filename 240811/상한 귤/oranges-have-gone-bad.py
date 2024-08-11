from collections import deque
n,k = map(int,input().split())
board = [[*map(int,input().split())]for _ in range(n)]


q = deque()
visited = [[-1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            q.append([i,j])
            visited[i][j] = 0

while q:
    x,y = q.popleft()
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        nx,ny = x + dx, y + dy
        if nx < 0 or nx >=n or ny <0 or ny>=n:continue
        if not board[nx][ny] or visited[nx][ny]!=-1:continue
        visited[nx][ny] = visited[x][y] + 1
        q.append([nx,ny])
for i in range(n):
    for j in range(n):
        v = visited[i][j]
        if board[i][j] == 1:
            if visited[i][j] == -1:
                v = -2
        print(v, end=' ')
    print()