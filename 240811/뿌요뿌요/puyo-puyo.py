n = int(input())

board = [[*map(int,input().split())]for _ in range(n)]

visited=[[0]*n for _ in range(n)]

v, ccnt = 0,0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:continue
        s = [(i,j)]
        visited[i][j] = 1
        cnt = 0
        while s:
            x,y = s.pop()
            cnt += 1
            for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                nx,ny = x +dx , y +dy
                if nx < 0 or nx >= n or ny < 0 or ny >=n:continue
                if board[nx][ny] != board[x][y] or visited[nx][ny]:continue
                visited[nx][ny] = 1
                s.append((nx,ny))
        ccnt = max(ccnt,cnt)
        if cnt > 3:
            v+=1
print(v,ccnt)