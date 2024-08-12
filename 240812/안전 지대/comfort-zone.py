n, m = map(int,input().split())

board = [[*map(int,input().split())] for _ in range(n)]

result = 0
resultk = 101
for k in range(1,100):
    now = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] or board[i][j] <= k:continue
            now += 1
            
            s = [(i,j)]
            visited[i][j] = 1
            while s:
                x,y = s.pop()
                for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                    nx,ny = x + dx ,y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >=m:continue
                    if board[nx][ny] <= k or visited[nx][ny]:continue
                    visited[nx][ny] = 1
                    s.append((nx,ny))
    if now > result:
        result = now
        resultk = k
print(resultk, result)